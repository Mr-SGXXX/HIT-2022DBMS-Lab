# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_dlg_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login_dlg(object):
    def setupUi(self, Login_dlg):
        Login_dlg.setObjectName("Login_dlg")
        Login_dlg.resize(436, 232)
        self.verticalLayout = QtWidgets.QVBoxLayout(Login_dlg)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.txt_password = QtWidgets.QLabel(Login_dlg)
        self.txt_password.setObjectName("txt_password")
        self.gridLayout.addWidget(self.txt_password, 3, 1, 1, 1)
        self.txt_account = QtWidgets.QLabel(Login_dlg)
        self.txt_account.setObjectName("txt_account")
        self.gridLayout.addWidget(self.txt_account, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(Login_dlg)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(Login_dlg)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 6, 1, 1)
        self.label_3 = QtWidgets.QLabel(Login_dlg)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(Login_dlg)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 3, 1, 1)
        self.le_phone = QtWidgets.QLineEdit(Login_dlg)
        self.le_phone.setEnabled(True)
        self.le_phone.setInputMask("")
        self.le_phone.setMaxLength(11)
        self.le_phone.setFrame(True)
        self.le_phone.setReadOnly(False)
        self.le_phone.setClearButtonEnabled(True)
        self.le_phone.setObjectName("le_phone")
        self.gridLayout.addWidget(self.le_phone, 1, 3, 1, 1)
        self.btn_register = QtWidgets.QPushButton(Login_dlg)
        self.btn_register.setObjectName("btn_register")
        self.gridLayout.addWidget(self.btn_register, 3, 5, 1, 1)
        self.cb_employee_login = QtWidgets.QCheckBox(Login_dlg)
        self.cb_employee_login.setObjectName("cb_employee_login")
        self.gridLayout.addWidget(self.cb_employee_login, 1, 5, 1, 1)
        self.label = QtWidgets.QLabel(Login_dlg)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(Login_dlg)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 3, 1, 1)
        self.le_password = QtWidgets.QLineEdit(Login_dlg)
        self.le_password.setInputMask("")
        self.le_password.setMaxLength(32)
        self.le_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.le_password.setClearButtonEnabled(True)
        self.le_password.setObjectName("le_password")
        self.gridLayout.addWidget(self.le_password, 3, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(Login_dlg)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Login_dlg)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Login_dlg)
        self.buttonBox.accepted.connect(Login_dlg.accept)
        self.buttonBox.rejected.connect(Login_dlg.reject)
        QtCore.QMetaObject.connectSlotsByName(Login_dlg)

    def retranslateUi(self, Login_dlg):
        _translate = QtCore.QCoreApplication.translate
        Login_dlg.setWindowTitle(_translate("Login_dlg", "Login"))
        self.txt_password.setText(_translate("Login_dlg", "密码"))
        self.txt_account.setText(_translate("Login_dlg", "账号"))
        self.le_phone.setPlaceholderText(_translate("Login_dlg", "请输入用户手机号"))
        self.btn_register.setText(_translate("Login_dlg", "注册"))
        self.cb_employee_login.setText(_translate("Login_dlg", "工作人员"))
        self.le_password.setPlaceholderText(_translate("Login_dlg", "请输入用户密码"))
