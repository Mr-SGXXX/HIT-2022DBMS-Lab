import datetime
import time
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QMessageBox

from SQL.insert_data import insert_customer
from GUI.UI.register_dlg_ui import Ui_register_dlg
from SQL.get_data import Employee_information

class RegisterDlg(QDialog):
    def __init__(self):
        super(RegisterDlg, self).__init__()
        self.valid = False
        self.ui = Ui_register_dlg()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.ui.tbl_employee_msg.setSelectionBehavior(1)
        self.ui.tbl_employee_msg.setColumnWidth(0, 60)
        self.ui.tbl_employee_msg.setColumnWidth(1, 50)
        self.ui.tbl_employee_msg.setColumnWidth(2, 50)
        self.ui.tbl_employee_msg.setColumnWidth(3, 100)
        self.ui.tbl_employee_msg.setColumnWidth(4, 290)
        self.ui.tbl_employee_msg.horizontalHeader().setDisabled(True)
        self.ui.buttonBox.accepted.connect(self.register)
        self.ui.tbl_employee_msg.selectRow(0)
        t, rows = Employee_information()
        self.ui.l_time.setText(f"查询时间:{t}s")
        for i in range(len(rows)):
            row = rows[i]
            for j in range(5):
                self.ui.tbl_employee_msg.setItem(i, j, QTableWidgetItem(str(row[j]).strip(' ')))

    def register(self):
        if not self.ui.le_phone.text().isdigit() or len(self.ui.le_phone.text()) != 11 or \
                self.ui.le_password.text() == "" or not self.ui.le_age.text().isdigit() \
                or self.ui.le_name.text() == "":
            QMessageBox.warning(self, "信息错误", "请将个人信息正确填写完整", QMessageBox.Ok)
            return
        ephone = self.ui.tbl_employee_msg.selectedItems()[3].text()
        cphone = self.ui.le_phone.text()
        name = self.ui.le_name.text()
        sex = self.ui.cb_sex.currentText()
        age = self.ui.le_age.text()
        aim = self.ui.cb_need.currentText()
        password = self.ui.le_password.text()
        if len(password) == 0:
            QMessageBox.warning(self, "信息错误", "密码不能为空", QMessageBox.Ok)
        try:
            t = insert_customer(cphone, name, sex, age, aim, password, ephone)
        except Exception as e:
            print(e)
            QMessageBox.warning(self, "信息错误", "此电话号可能已被注册或信息不符合规范", QMessageBox.Ok)
            return
        QMessageBox.information(self, "注册成功", f"您已成功注册\n用时：{t}s", QMessageBox.Ok)
        self.valid = True
        self.accept()

    def accept(self) -> None:
        if self.valid:
            super().accept()




