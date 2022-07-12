from PyQt5.QtWidgets import QMainWindow, QAction, QMessageBox, QTableWidgetItem
import datetime
import time

from GUI.UI.main_window_E_ui import Ui_MainWindow_E
from GUI.UI.main_window_C_ui import Ui_MainWindowC
from GUI.frame.select_house_dlg import SelectHouseDlg
from GUI.frame.sell_house_info_dlg import SellHouseInfoDlg
from GUI.frame.Login_dlg import LoginDlg
from GUI.frame.change_password_dlg import ChangePasswordDlg
from GUI.frame.buyer_info_dlg import BuyerInfoDlg
from SQL.gen_data import translate_timestamp
from SQL.get_data import *
from SQL.update_data import *
from SQL.insert_data import insert_house, insert_record
from SQL.insert_data import connect_db, disconnect_db


def preprocess_and_show(rows, col_num, table_widget):
    for i in range(len(rows)):
        row = rows[i]
        row_ = []
        for j in range(col_num):
            if row[j] is True:
                row_.append("是")
            elif row[j] is False:
                row_.append("否")
            elif row[j] is None:
                row_.append("")
            else:
                row_.append(str(row[j]).strip(' '))
        for j in range(col_num):
            table_widget.setItem(i, j, QTableWidgetItem(row_[j]))


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.hid = None
        self.phone = ""
        self.isEmployee = False
        self.login_dlg = LoginDlg()
        self.login_dlg.signal_.connect(self.get_account)
        self.login_dlg.show()
        self.login_dlg.exec_()
        if self.isEmployee:
            self.ui = Ui_MainWindow_E()
            self.ui.setupUi(self)
            row = get_employee_title(self.phone)
            self.setWindowTitle("工作人员界面-当前登录：" + row[0].strip(" ") + "    " + row[1].strip(" "))
            self.ui.tbl_customer.setColumnWidth(0, 100)
            self.ui.tbl_customer.setColumnWidth(1, 70)
            self.ui.tbl_customer.setColumnWidth(2, 50)
            self.ui.tbl_customer.setColumnWidth(3, 50)
            self.ui.tbl_customer.setColumnWidth(4, 70)
            self.ui.tbl_customer.setColumnWidth(5, 100)
            self.ui.tbl_customer.setColumnWidth(6, 100)
            self.ui.tbl_customer.setColumnWidth(7, 70)
            self.ui.tbl_house.setColumnWidth(0, 70)
            self.ui.tbl_house.setColumnWidth(1, 150)
            self.ui.tbl_house.setColumnWidth(2, 70)
            self.ui.tbl_house.setColumnWidth(3, 70)
            self.ui.tbl_house.setColumnWidth(4, 80)
            self.ui.tbl_house.setColumnWidth(5, 100)
            self.ui.tbl_house.setColumnWidth(6, 70)
            self.ui.tbl_house.setColumnWidth(7, 70)
            self.ui.tbl_house.setColumnWidth(8, 150)
            self.ui.tbl_buyer_info.setColumnWidth(0, 100)
            self.ui.tbl_buyer_info.setColumnWidth(1, 150)
            self.ui.tbl_buyer_info.setColumnWidth(2, 70)
            self.ui.tbl_buyer_info.setColumnWidth(3, 70)
            self.ui.tbl_buyer_info.setColumnWidth(4, 70)
            self.ui.tbl_buyer_info.setColumnWidth(5, 150)
            self.ui.tbl_record.setColumnWidth(0, 100)
            self.ui.tbl_record.setColumnWidth(1, 100)
            self.ui.tbl_record.setColumnWidth(2, 80)
            self.ui.tbl_record.setColumnWidth(3, 70)
            self.ui.tbl_record.setColumnWidth(4, 70)
            self.ui.tbl_record.setColumnWidth(5, 150)
            conn = connect_db()
            cur = conn.cursor()
            start_time = time.time()
            cur.execute("Select * from customer")
            end_time = time.time()
            self.ui.l_customer_time.setText(f"查询时间：{end_time - start_time}s")
            rows = cur.fetchall()
            preprocess_and_show(rows, 8, self.ui.tbl_customer)
            start_time = time.time()
            cur.execute("select * from house")
            end_time = time.time()
            self.ui.l_house_time.setText(f"查询时间：{end_time - start_time}s")
            rows = cur.fetchall()
            preprocess_and_show(rows, 9, self.ui.tbl_house)
            start_time = time.time()
            cur.execute("select * from buyer_msg")
            end_time = time.time()
            self.ui.l_buyer_msg_time.setText(f"查询时间：{end_time - start_time}s")
            rows = cur.fetchall()
            preprocess_and_show(rows, 6, self.ui.tbl_buyer_info)
            start_time = time.time()
            cur.execute("select * from record")
            end_time = time.time()
            self.ui.l_record_time.setText(f"查询时间：{end_time - start_time}s")
            rows = cur.fetchall()
            preprocess_and_show(rows, 6, self.ui.tbl_record)
            disconnect_db(conn)
        else:
            self.ui = Ui_MainWindowC()
            self.ui.setupUi(self)
            self.ui.menu.triggered[QAction].connect(self.process_trigger)
            self.welcome()
            self.ui.stackedPages.setCurrentIndex(0)
            self.account_page()
            self.ui.btn_house_trade.clicked.connect(self.buy_house)
            self.ui.btn_reg_house.clicked.connect(self.reg_house)
            self.ui.btn_change_password.clicked.connect(self.change_password)
            self.ui.btn_buyer_trade.clicked.connect(self.buyer_trade)
            self.ui.btn_release_sell_house.clicked.connect(self.release_sell_house_info)
            self.ui.btn_release_buyer_info.clicked.connect(self.release_buyer_info)

    def process_trigger(self, q: QAction):
        if q == self.ui.a_account_info:
            self.ui.stackedPages.setCurrentIndex(0)
            self.account_page()
        if q == self.ui.a_buyer_info:
            self.ui.stackedPages.setCurrentIndex(1)
            self.buyer_info_page()
        if q == self.ui.a_sell_house_info:
            self.ui.stackedPages.setCurrentIndex(2)
            self.sell_house_page()
        if q == self.ui.a_record:
            self.ui.stackedPages.setCurrentIndex(3)
            self.record_page()
        if q == self.ui.a_reg_house:
            self.ui.stackedPages.setCurrentIndex(4)
            self.reg_house_page()
        if q == self.ui.a_delete_account:
            self.delete_account()
        if q == self.ui.a_log_out:
            QMessageBox.information(self, "登出", "账户已登出\n感谢您的使用，再见", QMessageBox.Ok)
            exit(0)
        if q == self.ui.a_software_info:
            QMessageBox.information(self, "软件信息", "本程序由哈尔滨工业大学邵雨轩独立编写，仅用于数据库课程实验三\nUI实现：PyQT5\n数据库：PostgreSQL",
                                    QMessageBox.Ok)

    def delete_account(self):
        choice = QMessageBox.warning(self, "警告", "注销账号后无法登录，请您慎重考虑\n注意：账号注销后可以使用相同手机号重新注册并继承原账号交易记录\n如果您仍然决定注销请点击确定",
                                     QMessageBox.Ok | QMessageBox.Cancel)
        if choice == QMessageBox.Ok:
            t = delete_customer(self.phone)
            QMessageBox.information(self, "成功注销", f"您已经成功注销账号\n用时：{t}s", QMessageBox.Ok)
            exit(0)

    def account_page(self):
        self.ui.tbl_account_house.clearContents()
        info = get_customer_info(self.phone)
        self.ui.le_account_age.setText(info['age'])
        self.ui.le_account_sex.setText(info['sex'])
        self.ui.le_account_name.setText(info['cname'])
        self.ui.le_account_need.setText(info['aim'])
        self.ui.le_account_phone.setText(info['cphone'])
        self.ui.tbl_account_house.setColumnWidth(0, 120)
        self.ui.tbl_account_house.setColumnWidth(1, 70)
        self.ui.tbl_account_house.setColumnWidth(2, 50)
        self.ui.tbl_account_house.setColumnWidth(3, 70)
        self.ui.tbl_account_house.setColumnWidth(4, 70)
        self.ui.tbl_account_house.setColumnWidth(5, 70)
        self.ui.tbl_account_house.setColumnWidth(6, 160)
        self.ui.tbl_account_house.setColumnWidth(7, 171)
        t1, house_info = get_account_house_info(self.phone)
        t2, employee_info = get_single_employee_info(info['server'])
        self.ui.l_account_house_time.setText(f"查询时间：{t1 + t2}s")
        self.ui.le_account_ename.setText(employee_info['ename'])
        self.ui.le_account_esex.setText(employee_info['sex'])
        self.ui.le_account_ephone.setText(employee_info['ephone'])
        self.ui.le_account_emsg.setText(employee_info['information'])
        for i in range(len(house_info)):
            row = house_info[i]
            for j in range(8):
                self.ui.tbl_account_house.setItem(i, j, QTableWidgetItem(row[j]))
        self.ui.tbl_account_house.horizontalHeader().setDisabled(True)

    def buyer_info_page(self):
        self.ui.tbl_buyer_msg.clearContents()
        self.ui.tbl_buyer_msg.horizontalHeader().setDisabled(True)
        self.ui.tbl_buyer_msg.setColumnWidth(0, 100)
        self.ui.tbl_buyer_msg.setColumnWidth(1, 100)
        self.ui.tbl_buyer_msg.setColumnWidth(2, 70)
        self.ui.tbl_buyer_msg.setColumnWidth(3, 70)
        self.ui.tbl_buyer_msg.setColumnWidth(4, 100)
        self.ui.tbl_buyer_msg.setColumnWidth(5, 190)
        self.ui.tbl_buyer_msg.setColumnWidth(6, 151)
        self.ui.tbl_buyer_msg.selectRow(0)
        t, rows = get_buyer_info()
        self.ui.l_buyer_msg_time.setText(f"查询时间：{t}s")
        for i in range(len(rows)):
            row = rows[i]
            for j in range(7):
                self.ui.tbl_buyer_msg.setItem(i, j, QTableWidgetItem(str(row[j]).strip(" ")))

    def release_buyer_info(self):
        buyer_info_dlg = BuyerInfoDlg(self.phone)
        buyer_info_dlg.show()
        buyer_info_dlg.exec_()
        self.buyer_info_page()

    def buyer_trade(self):
        self.hid = None
        select_house_dlg = SelectHouseDlg(self.phone)
        select_house_dlg.signal_.connect(self.select_house)
        select_house_dlg.show()
        select_house_dlg.exec_()
        buyer_phone = self.ui.tbl_buyer_msg.selectedItems()[1].text()
        sell_or_rent = "租赁" if self.ui.tbl_buyer_msg.selectedItems()[2].text() == "租房" else "买卖"
        btime = self.ui.tbl_buyer_msg.selectedItems()[6].text()
        if self.hid is not None:
            t1 = delete_buyer_msg(buyer_phone, translate_timestamp(btime))
            t2 = update_buy_house(self.hid, buyer_phone)
            t3 = insert_record(self.phone, buyer_phone, self.hid, sell_or_rent,
                          self.ui.tbl_buyer_msg.selectedItems()[4].text(),
                          None)
            QMessageBox.information(self, "成功", f"您已成功出售或出租该房屋\n用时：{t1 + t2 + t3}s", QMessageBox.Ok)
            self.buyer_info_page()

    def select_house(self, hid):
        self.hid = hid

    def sell_house_page(self):
        self.ui.tbl_house_sell.clearContents()
        self.ui.tbl_house_sell.horizontalHeader().setDisabled(True)
        self.ui.tbl_house_sell.setColumnWidth(0, 100)
        self.ui.tbl_house_sell.setColumnWidth(1, 70)
        self.ui.tbl_house_sell.setColumnWidth(2, 80)
        self.ui.tbl_house_sell.setColumnWidth(3, 100)
        self.ui.tbl_house_sell.setColumnWidth(4, 86)
        self.ui.tbl_house_sell.setColumnWidth(5, 85)
        self.ui.tbl_house_sell.setColumnWidth(6, 130)
        self.ui.tbl_house_sell.setColumnWidth(7, 130)
        self.ui.tbl_house_sell.selectRow(0)
        t, self.rows = get_sell_house_info()
        self.ui.l_house_sell_time.setText(f"查询时间：{t}s")
        for i in range(len(self.rows)):
            row = self.rows[i]
            for j in range(8):
                self.ui.tbl_house_sell.setItem(i, j, QTableWidgetItem(row[j]))

    def release_sell_house_info(self):
        sell_info_dlg = SellHouseInfoDlg(self.phone)
        sell_info_dlg.show()
        sell_info_dlg.exec_()
        self.sell_house_page()

    def buy_house(self):
        rst = QMessageBox.information(self, "确认", "是否确认购买或租入房屋", QMessageBox.Ok | QMessageBox.Cancel)
        if rst == QMessageBox.Ok:
            house_info = self.rows[self.ui.tbl_house_sell.selectedItems()[0].row()]
            sell_or_rent = "租赁" if house_info[4] == "出租" else "买卖"
            t1 = insert_record(house_info[3], self.phone, house_info[8], sell_or_rent, house_info[5], None)
            t2 = update_buy_house(house_info[8], self.phone)
            QMessageBox.information(self, "成功", f"您已成功购买或租入该房屋\n用时：{t1 + t2}s", QMessageBox.Ok)
            self.sell_house_page()

    def record_page(self):
        self.ui.tbl_record.horizontalHeader().setDisabled(True)
        self.ui.tbl_record.setColumnWidth(0, 100)
        self.ui.tbl_record.setColumnWidth(1, 100)
        self.ui.tbl_record.setColumnWidth(2, 70)
        self.ui.tbl_record.setColumnWidth(3, 100)
        self.ui.tbl_record.setColumnWidth(4, 70)
        self.ui.tbl_record.setColumnWidth(5, 60)
        self.ui.tbl_record.setColumnWidth(6, 100)
        self.ui.tbl_record.setColumnWidth(7, 157)
        t, rows = get_record(self.phone)
        self.ui.l_record_time.setText(f"查询时间：{t}s")
        for i in range(len(rows)):
            row = rows[i]
            for j in range(8):
                self.ui.tbl_record.setItem(i, j, QTableWidgetItem(row[j]))

    def reg_house_page(self):
        self.ui.le_reg_house_loc.setText("")
        self.ui.le_reg_house_value.setText("")
        self.ui.le_reg_house_area.setText("")
        self.ui.cb_is_reno.setCurrentIndex(0)

    def reg_house(self):
        loc = self.ui.le_reg_house_loc.text()
        area = self.ui.le_reg_house_area.text()
        value = self.ui.le_reg_house_value.text()
        is_reno = True if self.ui.cb_is_reno.currentText() == "是" else False
        if not (area.isdigit() and int(area) > 0) or not (value.isdigit() and int(value) > 0) or len(loc) == 0:
            QMessageBox.warning(self, "错误", "输入的房屋注册信息有误，请重新输入", QMessageBox.Ok)
            return
        try:
            t = insert_house(loc, area, is_reno, value, self.phone)
            QMessageBox.information(self, "成功", f"房屋注册成功\n用时：{t}s", QMessageBox.Ok)
        except:
            QMessageBox.warning(self, "错误", "输入的房屋注册信息有误，请重新输入", QMessageBox.Ok)

    def change_password(self):
        change_password_dlg = ChangePasswordDlg(self.phone)
        change_password_dlg.show()
        change_password_dlg.exec_()

    def welcome(self):
        name, sex = get_customer_name_sex(self.phone)
        now = datetime.datetime.now()
        if sex == "男":
            sex = "先生"
        else:
            sex = "女士"
        if 6 <= now.hour < 11:
            time = "上午"
        elif 11 <= now.hour < 13:
            time = "中午"
        elif 13 <= now.hour < 18:
            time = "下午"
        elif 18 <= now.hour:
            time = "晚上"
        else:
            time = "凌晨"
        self.ui.l_welcome.setText(name + sex + "，" + time + "好")

    def get_account(self, is_employee, phone):
        self.isEmployee = is_employee
        self.phone = phone
