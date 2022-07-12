import time

from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem
from PyQt5.QtCore import pyqtSignal

from GUI.UI.select_house_ui import Ui_select_house_dlg
from SQL.get_data import get_account_house_info


class SelectHouseDlg(QDialog):
    signal_ = pyqtSignal(int)

    def __init__(self, sphone):
        super(SelectHouseDlg, self).__init__()
        self.ui = Ui_select_house_dlg()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.valid = False
        self.sphone = sphone
        self.ui.buttonBox.accepted.connect(self.trade)
        self.ui.tbl_select_house.horizontalHeader().setDisabled(True)
        self.ui.tbl_select_house.setColumnWidth(0, 200)
        self.ui.tbl_select_house.setColumnWidth(1, 100)
        self.ui.tbl_select_house.setColumnWidth(2, 70)
        self.ui.tbl_select_house.setColumnWidth(3, 120)
        t, self.house_info = get_account_house_info(self.sphone)
        self.ui.l_time.setText(f"查询时间：{t}s")
        for i in range(len(self.house_info)):
            row = self.house_info[i]
            for j in range(4):
                self.ui.tbl_select_house.setItem(i, j, QTableWidgetItem(row[j]))

    def trade(self):
        choice = QMessageBox.warning(self, "确认", "是否确认选择房屋", QMessageBox.Ok | QMessageBox.Cancel)
        if choice == QMessageBox.Ok:
            self.valid = True
            try:
                index = self.ui.tbl_select_house.selectedItems()[0].row()
                self.signal_.emit(int(self.house_info[index][8]))
                self.accept()
            except:
                QMessageBox.critical(self, "错误", "您没有选择任何房屋", QMessageBox.Ok)

    def accept(self) -> None:
        if self.valid:
            super().accept()
