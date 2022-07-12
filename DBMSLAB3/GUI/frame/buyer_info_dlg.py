from PyQt5.QtWidgets import QDialog, QMessageBox

from GUI.UI.buyer_info_dlg_ui import Ui_buyer_info_dlg
from SQL.insert_data import insert_buyer_msg


class BuyerInfoDlg(QDialog):
    def __init__(self, phone):
        super(BuyerInfoDlg, self).__init__()
        self.valid = False
        self.phone = phone
        self.ui = Ui_buyer_info_dlg()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.releaseInfo)

    def releaseInfo(self):
        choice = QMessageBox.information(self, "确认", "是否发布求租购信息", QMessageBox.Ok | QMessageBox.Cancel)
        if choice == QMessageBox.Ok:
            self.valid = True
            price = self.ui.le_price.text()
            moremsg = self.ui.le_moremsg.text()
            area = self.ui.le_area.text()
            if not (price.isdigit() and int(price) > 0) or not (area.isdigit() and int(area) > 0):
                QMessageBox.critical(self, "错误", "请将信息填写完整", QMessageBox.Ok)
                return
            t = insert_buyer_msg(self.phone, None, self.ui.cb_buy_or_rent.currentText(), price, area, moremsg)
            QMessageBox.information(self, "成功", f"您已成功发布求租购信息\n用时：{t}s", QMessageBox.Ok)
            self.accept()

    def accept(self) -> None:
        if self.valid:
            super().accept()
