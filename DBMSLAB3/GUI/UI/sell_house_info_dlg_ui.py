# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sell_house_info_dlg_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_select_house_dlg(object):
    def setupUi(self, select_house_dlg):
        select_house_dlg.setObjectName("select_house_dlg")
        select_house_dlg.resize(639, 385)
        self.gridLayout_3 = QtWidgets.QGridLayout(select_house_dlg)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_5 = QtWidgets.QLabel(select_house_dlg)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 7, 4, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_13 = QtWidgets.QLabel(select_house_dlg)
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 1, 3, 1, 1)
        self.l_price = QtWidgets.QLabel(select_house_dlg)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.l_price.setFont(font)
        self.l_price.setObjectName("l_price")
        self.gridLayout.addWidget(self.l_price, 1, 4, 1, 1)
        self.l_sell_or_rent = QtWidgets.QLabel(select_house_dlg)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.l_sell_or_rent.setFont(font)
        self.l_sell_or_rent.setObjectName("l_sell_or_rent")
        self.gridLayout.addWidget(self.l_sell_or_rent, 1, 0, 1, 1)
        self.cb_sell_or_rent = QtWidgets.QComboBox(select_house_dlg)
        self.cb_sell_or_rent.setObjectName("cb_sell_or_rent")
        self.cb_sell_or_rent.addItem("")
        self.cb_sell_or_rent.addItem("")
        self.gridLayout.addWidget(self.cb_sell_or_rent, 1, 2, 1, 1)
        self.le_price = QtWidgets.QLineEdit(select_house_dlg)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.le_price.setFont(font)
        self.le_price.setObjectName("le_price")
        self.gridLayout.addWidget(self.le_price, 1, 5, 1, 1)
        self.label_7 = QtWidgets.QLabel(select_house_dlg)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 2, 1, 1, 2)
        self.label_14 = QtWidgets.QLabel(select_house_dlg)
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 8, 4, 6, 1)
        self.label_8 = QtWidgets.QLabel(select_house_dlg)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 7, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(select_house_dlg)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(select_house_dlg)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 4, 1, 1)
        self.label_10 = QtWidgets.QLabel(select_house_dlg)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 6, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(select_house_dlg)
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 3, 1, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(select_house_dlg)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_3.addWidget(self.buttonBox, 12, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(select_house_dlg)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.l_moremsg = QtWidgets.QLabel(select_house_dlg)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.l_moremsg.setFont(font)
        self.l_moremsg.setObjectName("l_moremsg")
        self.horizontalLayout.addWidget(self.l_moremsg)
        self.le_moremsg = QtWidgets.QLineEdit(select_house_dlg)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.le_moremsg.setFont(font)
        self.le_moremsg.setObjectName("le_moremsg")
        self.horizontalLayout.addWidget(self.le_moremsg)
        self.gridLayout_3.addLayout(self.horizontalLayout, 4, 1, 1, 2)
        self.label = QtWidgets.QLabel(select_house_dlg)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 2, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(select_house_dlg)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 10, 2, 1, 1)
        self.l_select_house = QtWidgets.QLabel(select_house_dlg)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.l_select_house.setFont(font)
        self.l_select_house.setAlignment(QtCore.Qt.AlignCenter)
        self.l_select_house.setObjectName("l_select_house")
        self.gridLayout_3.addWidget(self.l_select_house, 0, 1, 1, 2)
        self.tbl_select_house = QtWidgets.QTableWidget(select_house_dlg)
        self.tbl_select_house.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbl_select_house.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbl_select_house.setRowCount(10000)
        self.tbl_select_house.setObjectName("tbl_select_house")
        self.tbl_select_house.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_select_house.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_select_house.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_select_house.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_select_house.setHorizontalHeaderItem(3, item)
        self.tbl_select_house.verticalHeader().setVisible(False)
        self.gridLayout_3.addWidget(self.tbl_select_house, 8, 2, 1, 1)
        self.l_house_select = QtWidgets.QLabel(select_house_dlg)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.l_house_select.setFont(font)
        self.l_house_select.setObjectName("l_house_select")
        self.gridLayout_3.addWidget(self.l_house_select, 7, 2, 1, 1)
        self.l_time = QtWidgets.QLabel(select_house_dlg)
        self.l_time.setObjectName("l_time")
        self.gridLayout_3.addWidget(self.l_time, 11, 2, 1, 1)

        self.retranslateUi(select_house_dlg)
        self.buttonBox.accepted.connect(select_house_dlg.accept)
        self.buttonBox.rejected.connect(select_house_dlg.reject)
        QtCore.QMetaObject.connectSlotsByName(select_house_dlg)

    def retranslateUi(self, select_house_dlg):
        _translate = QtCore.QCoreApplication.translate
        select_house_dlg.setWindowTitle(_translate("select_house_dlg", "选择房屋"))
        self.l_price.setText(_translate("select_house_dlg", "价格"))
        self.l_sell_or_rent.setText(_translate("select_house_dlg", "出租/售"))
        self.cb_sell_or_rent.setItemText(0, _translate("select_house_dlg", "出租"))
        self.cb_sell_or_rent.setItemText(1, _translate("select_house_dlg", "出售"))
        self.l_moremsg.setText(_translate("select_house_dlg", "备注 "))
        self.label_6.setText(_translate("select_house_dlg", "提示：如果选择先前已发布过信息的房屋，再次发布时将覆盖原信息"))
        self.l_select_house.setText(_translate("select_house_dlg", "请填写您的出租出售信息"))
        item = self.tbl_select_house.horizontalHeaderItem(0)
        item.setText(_translate("select_house_dlg", "地址"))
        item = self.tbl_select_house.horizontalHeaderItem(1)
        item.setText(_translate("select_house_dlg", "面积"))
        item = self.tbl_select_house.horizontalHeaderItem(2)
        item.setText(_translate("select_house_dlg", "是否精装"))
        item = self.tbl_select_house.horizontalHeaderItem(3)
        item.setText(_translate("select_house_dlg", "价值"))
        self.l_house_select.setText(_translate("select_house_dlg", "房屋选择"))
        self.l_time.setText(_translate("select_house_dlg", "查询时间：0.0s"))