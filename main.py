# -*- coding: utf-8 -*-
import os
import sys
from urllib.error import URLError, HTTPError

from PySide6.QtWidgets import *
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QFontMetrics

from api.contest import get_contest_problems
from api.problem import get_html, get_markdown
from api.submit import getAvailableLanguages, submit
from api.utils import get_username_from_cookiejar, load_cookies
from dlgLogin import dlgLogin
from submissionWatchThread import SubmissionWatchThread
from ui_MainWindow import Ui_MainWindow

__version__ = '0.3.1'
app = QApplication(sys.argv)

class ACHelperMainWindow(QMainWindow):
    SUPPORTED_MARKDOWN_FILTERS = 'Markdown 文件(*.md;*.markdown;*.mmd;*.mdwn;*.mdown);;文本文件(*.txt);;所有文件(*.*)'

    def __init__(self, parent=None):
        super().__init__(parent)

        # Initialize window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.statusbar.showMessage(f'欢迎使用 AtCoder Contest Helper {__version__}!')
        self.ui.codeEdit.setTabStopDistance(QFontMetrics(self.ui.codeEdit.font()).horizontalAdvance(' ') * 4)

        # Initialize table
        self.ui.contestTable.setHorizontalHeaderLabels(['题号', '标题', '时间限制', '空间限制'])
        self.ui.contestTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Initialize settings folder
        appdata = os.getenv('LOCALAPPDATA') if sys.platform == 'win32' else '/'
        self.settings_path = os.path.join(appdata, 'ACHelper')
        self.ui.labSettingsPath.setText(f'配置文件路径：{self.settings_path}')

        # Initialize cookie jar
        self.cookies_path = os.path.join(self.settings_path, 'cookies.txt')
        if os.path.exists(self.cookies_path): # already logged in?
            self.cookiejar = load_cookies(self.cookies_path)
            self.ui.labCurrentUser.setText(f'当前用户：{get_username_from_cookiejar(self.cookiejar)}')
        else:
            self.cookies_path = None

    @Slot()
    def on_actContest_Fetch_triggered(self):
        contestId = self.ui.contestIdEdit.text()
        try:
            problems = get_contest_problems(contestId, self.cookiejar)
        except HTTPError:
            errorInfo = f'比赛不存在：{contestId}'
            self.ui.statusbar.showMessage(f'错误：{errorInfo}')
            QMessageBox.critical(self, '错误', errorInfo)
            return
        except URLError:
            self.ui.statusbar.showMessage('网络错误')
            QMessageBox.critical(self, '错误', '网络错误。请检查网络连接，然后再试。')
            return
        self.ui.contestTable.setRowCount(len(problems))
        for row, (pid, taskid, title, tl, ml) in enumerate(problems):
            item = QTableWidgetItem(taskid)
            item.setData(Qt.UserRole, pid)
            self.ui.contestTable.setItem(row, 0, item)
            self.ui.contestTable.setItem(row, 1, QTableWidgetItem(title))
            self.ui.contestTable.setItem(row, 2, QTableWidgetItem(tl))
            self.ui.contestTable.setItem(row, 3, QTableWidgetItem(ml))
        for row in range(self.ui.contestTable.rowCount()):
            for col in range(self.ui.contestTable.columnCount()):
                self.ui.contestTable.item(row, col).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.ui.statusbar.showMessage(f'成功：获取比赛信息：{contestId}')

    @Slot()
    def on_actProblem_Fetch_triggered(self):
        contestId = self.ui.contestIdEdit_2.text()
        problemId = self.ui.problemIdEdit_2.text()
        url = f'https://atcoder.jp/contests/{contestId}/tasks/{problemId}'
        try:
            self.ui.problemBrowser.setHtml(get_html(url, self.cookiejar))
        except HTTPError:
            QMessageBox.critical(self, '错误', '题目不存在')
            self.ui.statusbar.showMessage('错误：题目不存在')
            return
        except URLError:
            self.ui.statusbar.showMessage('网络错误')
            QMessageBox.critical(self, '错误', '网络错误。请检查网络连接，然后再试。')
            return
        self.ui.statusbar.showMessage(f'成功：已加载题面：{url}')

    @Slot()
    def on_btnSaveAsMarkdown_clicked(self):
        filename, _ = QFileDialog.getSaveFileName(self, '保存', filter=self.SUPPORTED_MARKDOWN_FILTERS)
        if filename:
            contestId = self.ui.contestIdEdit_2.text()
            problemId = self.ui.problemIdEdit_2.text()
            with open(filename, 'w', encoding='utf-8') as file:
                get_markdown(f'https://atcoder.jp/contests/{contestId}/tasks/{problemId}', file, self.cookiejar)
            self.ui.statusbar.showMessage(f'题面已保存至 {filename}')

    @Slot()
    def on_contestTable_itemSelectionChanged(self):
        row = self.ui.contestTable.currentRow()
        col = self.ui.contestTable.currentColumn()
        if col < 2:
            self.ui.tabWidget.setCurrentIndex(1)
            self.ui.contestIdEdit_2.setText(self.ui.contestIdEdit.text())
            self.ui.problemIdEdit_2.setText(self.ui.contestTable.item(row, 0).data(Qt.UserRole))
            self.on_actProblem_Fetch_triggered()

    @Slot()
    def on_actSubmit_getLanguages_triggered(self):
        if not self.cookiejar:
            QMessageBox.critical(self, '错误', '请先登录再使用此功能。')
            return
        contestId = self.ui.contestIdEdit_3.text()
        problemId = self.ui.problemIdEdit_3.text()
        self.ui.comboBox_language.clear()
        for lid, language in getAvailableLanguages(contestId, problemId, self.cookiejar):
            self.ui.comboBox_language.addItem(language, lid)
        self.ui.comboBox_language.setCurrentIndex(2) # C++ (GCC 9.2.1)

    @Slot()
    def on_btnLogin_clicked(self):
        dialog = dlgLogin(self)
        if dialog.exec() == QDialog.Accepted:
            self.cookiejar = dialog.cookiejar
            self.ui.labCurrentUser.setText(f'当前用户：{dialog.ui.usernameEdit.text()}')
            # save new cookies
            if not os.path.exists(self.settings_path):
                os.mkdir(self.settings_path)
            self.cookiejar.save(self.cookies_path)

    @Slot()
    def on_btnJumpToContest_clicked(self):
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.contestIdEdit.setText(self.ui.contestIdEdit_2.text())
        self.on_actContest_Fetch_triggered()

    @Slot()
    def on_btnSubmitCode_clicked(self):
        self.ui.tabWidget.setCurrentIndex(2)
        self.ui.contestIdEdit_3.setText(self.ui.contestIdEdit_2.text())
        self.ui.problemIdEdit_3.setText(self.ui.problemIdEdit_2.text())
        self.on_actSubmit_getLanguages_triggered()

    @Slot()
    def on_btnSubmit_clicked(self):
        if self.ui.comboBox_language.count() == 0:
            QMessageBox.critical(self, '错误', '请选择一个语言。')
            return
        contest = self.ui.contestIdEdit_3.text()
        problem = self.ui.problemIdEdit_3.text()
        code = self.ui.codeEdit.toPlainText()
        language = self.ui.comboBox_language.currentData()
        try:
            sid = submit(contest, problem, code, language, self.cookiejar)
        except ValueError:
            QMessageBox.critical(self, '错误', '提交失败。可能为AHC的提交频率限制所导致，具体参考AtCoder Heurstic Contest比赛规则。')
            return
        self.ui.statusbar.showMessage(f'提交成功。提交记录 ID: {sid}')
        self.ui.btnSubmit.setEnabled(False)
        thread = SubmissionWatchThread(contest, sid, self.cookiejar, self)
        thread.updateSignal.connect(self.ui.statusbar.showMessage)
        thread.finished.connect(lambda: self.ui.btnSubmit.setEnabled(True))
        thread.start()

mainform = ACHelperMainWindow()
mainform.show()

sys.exit(app.exec())