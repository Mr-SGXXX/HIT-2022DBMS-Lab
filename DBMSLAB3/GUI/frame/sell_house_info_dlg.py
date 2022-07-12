import time

from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem

from GUI.UI.sell_house_info_dlg_ui import Ui_select_house_dlg
from SQL.get_data import get_account_house_info
from SQL.insert_data import insert_sell_house

class SellHouseInfoDlg(QDialog):
    def __init__(self, phone):
        super(SellHouseInfoDlg, self).__init__()
        self.ui = Ui_select_house_dlg()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.valid = False
        self.phone = phone
        self.ui.buttonBox.accepted.connect(self.release_info)
        self.ui.tbl_select_house.horizontalHeader().setDisabled(True)
        self.ui.tbl_select_house.setColumnWidth(0, 200)
        self.ui.tbl_select_house.setColumnWidth(1, 100)
        self.ui.tbl_select_house.setColumnWidth(2, 70)
        self.ui.tbl_select_house.setColumnWidth(3, 168)
        t, self.house_info = get_account_house_info(self.phone)
        self.ui.l_time.setText(f"查询时间：{t}s")
        for i in range(len(self.house_info)):
            row = self.house_info[i]
            for j in range(4):
                self.ui.tbl_select_house.setItem(i, j, QTableWidgetItem(row[j]))

    def release_info(self):
        choice = QMessageBox.information(self, "确认", "是否发布房租出租出售信息", QMessageBox.Ok | QMessageBox.Cancel)
        if choice == QMessageBox.Ok:
            self.valid = True
            try:
                index = self.ui.tbl_select_house.selectedItems()[0].row()
                sell_or_rent = self.ui.cb_sell_or_rent.currentText()
                price = self.ui.le_price.text()
                moremsg = self.ui.le_moremsg.text()
                if not (price.isdigit() and int(price) > 0):
                    QMessageBox.critical(self, "错误", "请将信息填写完整", QMessageBox.Ok)
                    return
                hid = int(self.house_info[index][8])
                t = insert_sell_house(hid, sell_or_rent, price, None, moremsg)
                QMessageBox.information(self, "成功", f"您已成功发布房屋出租出售信息\n用时：{t}s", QMessageBox.Ok)
                self.accept()
            except:
                QMessageBox.critical(self, "错误", "您没有选择任何房屋", QMessageBox.Ok)

    def accept(self) -> None:
        if self.valid:
            super().accept()
