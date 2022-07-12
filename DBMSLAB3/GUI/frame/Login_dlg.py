from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDialog, QMessageBox

from GUI.UI.login_dlg_ui import Ui_Login_dlg
from GUI.frame.Register_dlg import RegisterDlg
from SQL.get_data import *


class LoginDlg(QDialog):
    signal_ = pyqtSignal(bool, str)

    def __init__(self):
        super(LoginDlg, self).__init__()
        self.ui = Ui_Login_dlg()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.ui.buttonBox.accepted.connect(self.check_available)
        self.ui.btn_register.clicked.connect(self.register)
        self.available = False

    def register(self):
        register_dlg = RegisterDlg()
        register_dlg.show()
        register_dlg.exec_()

    def check_available(self):
        phone = self.ui.le_phone.text()
        password = self.ui.le_password.text()
        if phone == "" or password == "":
            QMessageBox.warning(self, "信息错误", "账号或密码错误，请重新输入", QMessageBox.Ok)
            return
        try:
            if self.ui.cb_employee_login.isChecked():
                # 检索是不是工作人员
                t, find = Employee_login(phone, password)
            else:
                # 检索是不是客户
                t, find = Customer_login(phone, password)
            if find:
                self.available = True
                QMessageBox.information(self, "登陆成功", f"您已登陆成功\n用时：{t}s", QMessageBox.Ok)
                self.accept()
            else:
                QMessageBox.warning(self, "信息错误", f"账号或密码错误，请重新输入\n用时：{t}s", QMessageBox.Ok)
        except:
            QMessageBox.warning(self, "信息错误", "账号或密码错误，请重新输入", QMessageBox.Ok)

    def accept(self) -> None:
        if self.available:
            self.signal_.emit(self.ui.cb_employee_login.isChecked(), self.ui.le_phone.text())
            super().accept()

    def reject(self) -> None:
        exit(0)
