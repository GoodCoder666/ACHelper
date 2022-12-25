# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextBrowser, QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        icon = QIcon()
        icon.addFile(u":/images/icons/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actContest_Fetch = QAction(MainWindow)
        self.actContest_Fetch.setObjectName(u"actContest_Fetch")
        self.actProblem_Fetch = QAction(MainWindow)
        self.actProblem_Fetch.setObjectName(u"actProblem_Fetch")
        self.actSubmit_getLanguages = QAction(MainWindow)
        self.actSubmit_getLanguages.setObjectName(u"actSubmit_getLanguages")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.contestTab = QWidget()
        self.contestTab.setObjectName(u"contestTab")
        self.verticalLayout = QVBoxLayout(self.contestTab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labContestId = QLabel(self.contestTab)
        self.labContestId.setObjectName(u"labContestId")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labContestId.sizePolicy().hasHeightForWidth())
        self.labContestId.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.labContestId)

        self.contestIdEdit = QLineEdit(self.contestTab)
        self.contestIdEdit.setObjectName(u"contestIdEdit")

        self.horizontalLayout.addWidget(self.contestIdEdit)

        self.btnFetchProblems = QPushButton(self.contestTab)
        self.btnFetchProblems.setObjectName(u"btnFetchProblems")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnFetchProblems.sizePolicy().hasHeightForWidth())
        self.btnFetchProblems.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.btnFetchProblems)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.contestTable = QTableWidget(self.contestTab)
        if (self.contestTable.columnCount() < 4):
            self.contestTable.setColumnCount(4)
        self.contestTable.setObjectName(u"contestTable")
        self.contestTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.contestTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.contestTable.setColumnCount(4)

        self.verticalLayout.addWidget(self.contestTable)

        self.tabWidget.addTab(self.contestTab, "")
        self.problemTab = QWidget()
        self.problemTab.setObjectName(u"problemTab")
        self.verticalLayout_2 = QVBoxLayout(self.problemTab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labContestId_2 = QLabel(self.problemTab)
        self.labContestId_2.setObjectName(u"labContestId_2")

        self.horizontalLayout_2.addWidget(self.labContestId_2)

        self.contestIdEdit_2 = QLineEdit(self.problemTab)
        self.contestIdEdit_2.setObjectName(u"contestIdEdit_2")

        self.horizontalLayout_2.addWidget(self.contestIdEdit_2)

        self.labProblemId_2 = QLabel(self.problemTab)
        self.labProblemId_2.setObjectName(u"labProblemId_2")

        self.horizontalLayout_2.addWidget(self.labProblemId_2)

        self.problemIdEdit_2 = QLineEdit(self.problemTab)
        self.problemIdEdit_2.setObjectName(u"problemIdEdit_2")

        self.horizontalLayout_2.addWidget(self.problemIdEdit_2)

        self.btnFetchProblem = QPushButton(self.problemTab)
        self.btnFetchProblem.setObjectName(u"btnFetchProblem")

        self.horizontalLayout_2.addWidget(self.btnFetchProblem)

        self.btnSaveAsMarkdown = QPushButton(self.problemTab)
        self.btnSaveAsMarkdown.setObjectName(u"btnSaveAsMarkdown")

        self.horizontalLayout_2.addWidget(self.btnSaveAsMarkdown)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.problemBrowser = QTextBrowser(self.problemTab)
        self.problemBrowser.setObjectName(u"problemBrowser")

        self.verticalLayout_2.addWidget(self.problemBrowser)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btnJumpToContest = QPushButton(self.problemTab)
        self.btnJumpToContest.setObjectName(u"btnJumpToContest")

        self.horizontalLayout_6.addWidget(self.btnJumpToContest)

        self.btnSubmitCode = QPushButton(self.problemTab)
        self.btnSubmitCode.setObjectName(u"btnSubmitCode")

        self.horizontalLayout_6.addWidget(self.btnSubmitCode)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.tabWidget.addTab(self.problemTab, "")
        self.submitTab = QWidget()
        self.submitTab.setObjectName(u"submitTab")
        self.verticalLayout_3 = QVBoxLayout(self.submitTab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.labContestId_3 = QLabel(self.submitTab)
        self.labContestId_3.setObjectName(u"labContestId_3")
        sizePolicy.setHeightForWidth(self.labContestId_3.sizePolicy().hasHeightForWidth())
        self.labContestId_3.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.labContestId_3)

        self.contestIdEdit_3 = QLineEdit(self.submitTab)
        self.contestIdEdit_3.setObjectName(u"contestIdEdit_3")

        self.horizontalLayout_4.addWidget(self.contestIdEdit_3)

        self.labProblemId_3 = QLabel(self.submitTab)
        self.labProblemId_3.setObjectName(u"labProblemId_3")

        self.horizontalLayout_4.addWidget(self.labProblemId_3)

        self.problemIdEdit_3 = QLineEdit(self.submitTab)
        self.problemIdEdit_3.setObjectName(u"problemIdEdit_3")

        self.horizontalLayout_4.addWidget(self.problemIdEdit_3)

        self.btnGetLanguages = QPushButton(self.submitTab)
        self.btnGetLanguages.setObjectName(u"btnGetLanguages")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btnGetLanguages.sizePolicy().hasHeightForWidth())
        self.btnGetLanguages.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.btnGetLanguages)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labLanguage = QLabel(self.submitTab)
        self.labLanguage.setObjectName(u"labLanguage")
        sizePolicy.setHeightForWidth(self.labLanguage.sizePolicy().hasHeightForWidth())
        self.labLanguage.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.labLanguage)

        self.comboBox_language = QComboBox(self.submitTab)
        self.comboBox_language.setObjectName(u"comboBox_language")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.comboBox_language.sizePolicy().hasHeightForWidth())
        self.comboBox_language.setSizePolicy(sizePolicy3)

        self.horizontalLayout_3.addWidget(self.comboBox_language)

        self.btnSubmit = QPushButton(self.submitTab)
        self.btnSubmit.setObjectName(u"btnSubmit")
        sizePolicy1.setHeightForWidth(self.btnSubmit.sizePolicy().hasHeightForWidth())
        self.btnSubmit.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.btnSubmit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.labSubmissionCode = QLabel(self.submitTab)
        self.labSubmissionCode.setObjectName(u"labSubmissionCode")

        self.verticalLayout_3.addWidget(self.labSubmissionCode)

        self.codeEdit = QPlainTextEdit(self.submitTab)
        self.codeEdit.setObjectName(u"codeEdit")
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(12)
        self.codeEdit.setFont(font)

        self.verticalLayout_3.addWidget(self.codeEdit)

        self.tabWidget.addTab(self.submitTab, "")
        self.settingsTab = QWidget()
        self.settingsTab.setObjectName(u"settingsTab")
        self.verticalLayout_4 = QVBoxLayout(self.settingsTab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.labCurrentUser = QLabel(self.settingsTab)
        self.labCurrentUser.setObjectName(u"labCurrentUser")

        self.horizontalLayout_5.addWidget(self.labCurrentUser)

        self.btnLogin = QPushButton(self.settingsTab)
        self.btnLogin.setObjectName(u"btnLogin")

        self.horizontalLayout_5.addWidget(self.btnLogin)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.labSettingsPath = QLabel(self.settingsTab)
        self.labSettingsPath.setObjectName(u"labSettingsPath")
        sizePolicy.setHeightForWidth(self.labSettingsPath.sizePolicy().hasHeightForWidth())
        self.labSettingsPath.setSizePolicy(sizePolicy)

        self.verticalLayout_4.addWidget(self.labSettingsPath)

        self.tabWidget.addTab(self.settingsTab, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.btnFetchProblems.clicked.connect(self.actContest_Fetch.trigger)
        self.contestIdEdit.returnPressed.connect(self.actContest_Fetch.trigger)
        self.problemIdEdit_2.returnPressed.connect(self.actProblem_Fetch.trigger)
        self.btnFetchProblem.clicked.connect(self.actProblem_Fetch.trigger)
        self.btnGetLanguages.clicked.connect(self.actSubmit_getLanguages.trigger)
        self.problemIdEdit_3.returnPressed.connect(self.actSubmit_getLanguages.trigger)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AtCoder Contest Helper", None))
        self.actContest_Fetch.setText(QCoreApplication.translate("MainWindow", u"\u83b7\u53d6\u6bd4\u8d5b\u9898\u76ee", None))
#if QT_CONFIG(tooltip)
        self.actContest_Fetch.setToolTip(QCoreApplication.translate("MainWindow", u"\u83b7\u53d6\u6bd4\u8d5b\u9898\u76ee", None))
#endif // QT_CONFIG(tooltip)
        self.actProblem_Fetch.setText(QCoreApplication.translate("MainWindow", u"\u83b7\u53d6\u9898\u9762", None))
        self.actSubmit_getLanguages.setText(QCoreApplication.translate("MainWindow", u"\u83b7\u53d6\u53ef\u7528\u8bed\u8a00", None))
        self.labContestId.setText(QCoreApplication.translate("MainWindow", u"\u6bd4\u8d5b ID:", None))
        self.btnFetchProblems.setText(QCoreApplication.translate("MainWindow", u"\u83b7\u53d6\u9898\u76ee", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.contestTab), QCoreApplication.translate("MainWindow", u"\u6bd4\u8d5b", None))
        self.labContestId_2.setText(QCoreApplication.translate("MainWindow", u"\u6bd4\u8d5b ID:", None))
        self.labProblemId_2.setText(QCoreApplication.translate("MainWindow", u"\u9898\u76ee ID:", None))
        self.btnFetchProblem.setText(QCoreApplication.translate("MainWindow", u"\u83b7\u53d6\u9898\u9762", None))
        self.btnSaveAsMarkdown.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u4e3aMarkdown", None))
        self.btnJumpToContest.setText(QCoreApplication.translate("MainWindow", u"\u8f6c\u5230\u6bd4\u8d5b", None))
        self.btnSubmitCode.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u4ea4\u4ee3\u7801", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.problemTab), QCoreApplication.translate("MainWindow", u"\u9898\u76ee", None))
        self.labContestId_3.setText(QCoreApplication.translate("MainWindow", u"\u6bd4\u8d5b ID:", None))
        self.labProblemId_3.setText(QCoreApplication.translate("MainWindow", u"\u9898\u76ee ID:", None))
        self.btnGetLanguages.setText(QCoreApplication.translate("MainWindow", u"\u83b7\u53d6\u53ef\u7528\u8bed\u8a00", None))
        self.labLanguage.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u4ea4\u8bed\u8a00:", None))
        self.btnSubmit.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u4ea4", None))
        self.labSubmissionCode.setText(QCoreApplication.translate("MainWindow", u"\u4ee3\u7801:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.submitTab), QCoreApplication.translate("MainWindow", u"\u63d0\u4ea4", None))
        self.labCurrentUser.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u7528\u6237\uff1a\u672a\u767b\u5f55", None))
        self.btnLogin.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5f55", None))
        self.labSettingsPath.setText(QCoreApplication.translate("MainWindow", u"\u914d\u7f6e\u6587\u4ef6\u4fdd\u5b58\u8def\u5f84\uff1a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settingsTab), QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
    # retranslateUi

