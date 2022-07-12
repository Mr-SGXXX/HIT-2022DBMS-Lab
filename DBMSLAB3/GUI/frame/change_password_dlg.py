from PyQt5.QtWidgets import QDialog, QMessageBox

from GUI.UI.change_password_ui import Ui_change_password_dlg
from SQL.update_data import change_password
from SQL.get_data import Customer_login


class ChangePasswordDlg(QDialog):
    def __init__(self, cphone):
        super(ChangePasswordDlg, self).__init__()
        self.ui = Ui_change_password_dlg()
        self.ui.setupUi(self)
        self.cphone = cphone
        self.valid = False
        self.ui.buttonBox.accepted.connect(self._change_password)

    def _change_password(self):
        if not Customer_login(self.cphone, self.ui.le_old_password.text()):
            QMessageBox.warning(self, "错误", "您的旧密码输入错误，请重试", QMessageBox.Ok)
            return
        if len(self.ui.le_new_password.text()) == 0:
            QMessageBox.warning(self, "信息错误", "密码不能为空", QMessageBox.Ok)
            return
        if self.ui.le_new_password.text() == self.ui.le_new_password_again.text():
            t = change_password(self.cphone, self.ui.le_new_password.text())
            QMessageBox.information(self, "成功", f"您已成功修改密码\n用时：{t}s", QMessageBox.Ok)
            self.valid = True
            self.accept()
        else:
            QMessageBox.warning(self, "错误", "两次输入的新密码不匹配", QMessageBox.Ok)

    def accept(self) -> None:
        if self.valid:
            super().accept()
