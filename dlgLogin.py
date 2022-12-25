# -*- coding: utf-8 -*-
from PySide6.QtWidgets import *
from ui_dlgLogin import Ui_Dialog
from api.login import login

class dlgLogin(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.buttonBox.button(QDialogButtonBox.Ok).setText('登录')
        self.ui.buttonBox.button(QDialogButtonBox.Cancel).setText('取消')

    def accept(self):
        username = self.ui.usernameEdit.text()
        password = self.ui.passwordEdit.text()
        try:
            self.cookiejar = login(username, password)
        except ValueError:
            QMessageBox.critical(self, '错误', '用户名或密码错误。请检查用户名和密码，然后再试。')
        except Exception:
            QMessageBox.critical(self, '错误', '网络错误。请检查网络设置，然后再试。')
        else:
            super().accept()