# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register_dlg_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_register_dlg(object):
    def setupUi(self, register_dlg):
        register_dlg.setObjectName("register_dlg")
        register_dlg.setEnabled(True)
        register_dlg.resize(591, 490)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(register_dlg)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.cb_sex = QtWidgets.QComboBox(register_dlg)
        self.cb_sex.setObjectName("cb_sex")
        self.cb_sex.addItem("")
        self.cb_sex.addItem("")
        self.gridLayout.addWidget(self.cb_sex, 5, 1, 1, 1)
        self.label = QtWidgets.QLabel(register_dlg)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 2, 1, 1)
        self.txt_phone = QtWidgets.QLabel(register_dlg)
        self.txt_phone.setObjectName("txt_phone")
        self.gridLayout.addWidget(self.txt_phone, 3, 0, 1, 1)
        self.le_phone = QtWidgets.QLineEdit(register_dlg)
        self.le_phone.setMaxLength(11)
        self.le_phone.setObjectName("le_phone")
        self.gridLayout.addWidget(self.le_phone, 3, 1, 1, 1)
        self.le_password = QtWidgets.QLineEdit(register_dlg)
        self.le_password.setMaxLength(32)
        self.le_password.setObjectName("le_password")
        self.gridLayout.addWidget(self.le_password, 3, 4, 1, 1)
        self.txt_sex = QtWidgets.QLabel(register_dlg)
        self.txt_sex.setObjectName("txt_sex")
        self.gridLayout.addWidget(self.txt_sex, 5, 0, 1, 1)
        self.le_name = QtWidgets.QLineEdit(register_dlg)
        self.le_name.setMaxLength(32)
        self.le_name.setObjectName("le_name")
        self.gridLayout.addWidget(self.le_name, 1, 1, 1, 1)
        self.txt_password = QtWidgets.QLabel(register_dlg)
        self.txt_password.setObjectName("txt_password")
        self.gridLayout.addWidget(self.txt_password, 3, 3, 1, 1)
        self.cb_need = QtWidgets.QComboBox(register_dlg)
        self.cb_need.setObjectName("cb_need")
        self.cb_need.addItem("")
        self.cb_need.addItem("")
        self.cb_need.addItem("")
        self.cb_need.addItem("")
        self.gridLayout.addWidget(self.cb_need, 5, 4, 1, 1)
        self.txt_need = QtWidgets.QLabel(register_dlg)
        self.txt_need.setObjectName("txt_need")
        self.gridLayout.addWidget(self.txt_need, 5, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(register_dlg)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(register_dlg)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.txt_age = QtWidgets.QLabel(register_dlg)
        self.txt_age.setObjectName("txt_age")
        self.gridLayout.addWidget(self.txt_age, 1, 3, 1, 1)
        self.txt_name = QtWidgets.QLabel(register_dlg)
        self.txt_name.setObjectName("txt_name")
        self.gridLayout.addWidget(self.txt_name, 1, 0, 1, 1)
        self.le_age = QtWidgets.QLineEdit(register_dlg)
        self.le_age.setMaxLength(3)
        self.le_age.setObjectName("le_age")
        self.gridLayout.addWidget(self.le_age, 1, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(register_dlg)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.label_5 = QtWidgets.QLabel(register_dlg)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(register_dlg)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.txt_employee = QtWidgets.QLabel(register_dlg)
        self.txt_employee.setObjectName("txt_employee")
        self.verticalLayout.addWidget(self.txt_employee)
        self.tbl_employee_msg = QtWidgets.QTableWidget(register_dlg)
        self.tbl_employee_msg.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbl_employee_msg.setDragEnabled(True)
        self.tbl_employee_msg.setDefaultDropAction(QtCore.Qt.TargetMoveAction)
        self.tbl_employee_msg.setShowGrid(True)
        self.tbl_employee_msg.setGridStyle(QtCore.Qt.SolidLine)
        self.tbl_employee_msg.setWordWrap(True)
        self.tbl_employee_msg.setRowCount(10000)
        self.tbl_employee_msg.setColumnCount(5)
        self.tbl_employee_msg.setObjectName("tbl_employee_msg")
        item = QtWidgets.QTableWidgetItem()
        self.tbl_employee_msg.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_employee_msg.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_employee_msg.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_employee_msg.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_employee_msg.setHorizontalHeaderItem(4, item)
        self.tbl_employee_msg.horizontalHeader().setVisible(True)
        self.tbl_employee_msg.horizontalHeader().setCascadingSectionResizes(True)
        self.tbl_employee_msg.horizontalHeader().setDefaultSectionSize(110)
        self.tbl_employee_msg.horizontalHeader().setHighlightSections(False)
        self.tbl_employee_msg.horizontalHeader().setMinimumSectionSize(21)
        self.tbl_employee_msg.verticalHeader().setVisible(False)
        self.tbl_employee_msg.verticalHeader().setDefaultSectionSize(25)
        self.tbl_employee_msg.verticalHeader().setSortIndicatorShown(False)
        self.tbl_employee_msg.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.tbl_employee_msg)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.l_time = QtWidgets.QLabel(register_dlg)
        self.l_time.setObjectName("l_time")
        self.verticalLayout_2.addWidget(self.l_time)
        self.buttonBox = QtWidgets.QDialogButtonBox(register_dlg)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(register_dlg)
        self.buttonBox.accepted.connect(register_dlg.accept)
        self.buttonBox.rejected.connect(register_dlg.reject)
        QtCore.QMetaObject.connectSlotsByName(register_dlg)

    def retranslateUi(self, register_dlg):
        _translate = QtCore.QCoreApplication.translate
        register_dlg.setWindowTitle(_translate("register_dlg", "注册"))
        self.cb_sex.setCurrentText(_translate("register_dlg", "男"))
        self.cb_sex.setItemText(0, _translate("register_dlg", "男"))
        self.cb_sex.setItemText(1, _translate("register_dlg", "女"))
        self.txt_phone.setText(_translate("register_dlg", "电话"))
        self.txt_sex.setText(_translate("register_dlg", "性别"))
        self.txt_password.setText(_translate("register_dlg", "密码"))
        self.cb_need.setItemText(0, _translate("register_dlg", "求租"))
        self.cb_need.setItemText(1, _translate("register_dlg", "出租"))
        self.cb_need.setItemText(2, _translate("register_dlg", "求购"))
        self.cb_need.setItemText(3, _translate("register_dlg", "卖房"))
        self.txt_need.setText(_translate("register_dlg", "需求"))
        self.txt_age.setText(_translate("register_dlg", "年龄"))
        self.txt_name.setText(_translate("register_dlg", "姓名"))
        self.txt_employee.setText(_translate("register_dlg", "专属客服"))
        self.tbl_employee_msg.setSortingEnabled(True)
        item = self.tbl_employee_msg.horizontalHeaderItem(0)
        item.setText(_translate("register_dlg", "姓名"))
        item = self.tbl_employee_msg.horizontalHeaderItem(1)
        item.setText(_translate("register_dlg", "性别"))
        item = self.tbl_employee_msg.horizontalHeaderItem(2)
        item.setText(_translate("register_dlg", "年龄"))
        item = self.tbl_employee_msg.horizontalHeaderItem(3)
        item.setText(_translate("register_dlg", "电话"))
        item = self.tbl_employee_msg.horizontalHeaderItem(4)
        item.setText(_translate("register_dlg", "个人信息"))
        self.l_time.setText(_translate("register_dlg", "查询时间：0.0s"))