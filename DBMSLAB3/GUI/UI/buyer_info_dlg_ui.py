# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'buyer_info_dlg_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_buyer_info_dlg(object):
    def setupUi(self, buyer_info_dlg):
        buyer_info_dlg.setObjectName("buyer_info_dlg")
        buyer_info_dlg.resize(561, 391)
        self.gridLayout_2 = QtWidgets.QGridLayout(buyer_info_dlg)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.l_buyer_info = QtWidgets.QLabel(buyer_info_dlg)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.l_buyer_info.setFont(font)
        self.l_buyer_info.setAlignment(QtCore.Qt.AlignCenter)
        self.l_buyer_info.setObjectName("l_buyer_info")
        self.gridLayout_2.addWidget(self.l_buyer_info, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.l_area = QtWidgets.QLabel(buyer_info_dlg)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.l_area.setFont(font)
        self.l_area.setObjectName("l_area")
        self.gridLayout.addWidget(self.l_area, 2, 0, 1, 1)
        self.cb_buy_or_rent = QtWidgets.QComboBox(buyer_info_dlg)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.cb_buy_or_rent.setFont(font)
        self.cb_buy_or_rent.setObjectName("cb_buy_or_rent")
        self.cb_buy_or_rent.addItem("")
        self.cb_buy_or_rent.addItem("")
        self.gridLayout.addWidget(self.cb_buy_or_rent, 0, 1, 1, 1)
        self.le_price = QtWidgets.QLineEdit(buyer_info_dlg)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.le_price.setFont(font)
        self.le_price.setObjectName("le_price")
        self.gridLayout.addWidget(self.le_price, 0, 4, 1, 1)
        self.l_moremsg = QtWidgets.QLabel(buyer_info_dlg)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.l_moremsg.setFont(font)
        self.l_moremsg.setAlignment(QtCore.Qt.AlignCenter)
        self.l_moremsg.setObjectName("l_moremsg")
        self.gridLayout.addWidget(self.l_moremsg, 2, 3, 1, 1)
        self.le_area = QtWidgets.QLineEdit(buyer_info_dlg)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.le_area.setFont(font)
        self.le_area.setObjectName("le_area")
        self.gridLayout.addWidget(self.le_area, 2, 1, 1, 1)
        self.le_moremsg = QtWidgets.QLineEdit(buyer_info_dlg)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.le_moremsg.setFont(font)
        self.le_moremsg.setObjectName("le_moremsg")
        self.gridLayout.addWidget(self.le_moremsg, 2, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(buyer_info_dlg)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)
        self.l_buy_or_rent = QtWidgets.QLabel(buyer_info_dlg)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.l_buy_or_rent.setFont(font)
        self.l_buy_or_rent.setAlignment(QtCore.Qt.AlignCenter)
        self.l_buy_or_rent.setObjectName("l_buy_or_rent")
        self.gridLayout.addWidget(self.l_buy_or_rent, 0, 0, 1, 1)
        self.l_price = QtWidgets.QLabel(buyer_info_dlg)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.l_price.setFont(font)
        self.l_price.setObjectName("l_price")
        self.gridLayout.addWidget(self.l_price, 0, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(buyer_info_dlg)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_7 = QtWidgets.QLabel(buyer_info_dlg)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.buttonBox = QtWidgets.QDialogButtonBox(buyer_info_dlg)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.label_9 = QtWidgets.QLabel(buyer_info_dlg)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.gridLayout_2.addLayout(self.verticalLayout, 2, 0, 1, 1)

        self.retranslateUi(buyer_info_dlg)
        self.buttonBox.accepted.connect(buyer_info_dlg.accept)
        self.buttonBox.rejected.connect(buyer_info_dlg.reject)
        QtCore.QMetaObject.connectSlotsByName(buyer_info_dlg)

    def retranslateUi(self, buyer_info_dlg):
        _translate = QtCore.QCoreApplication.translate
        buyer_info_dlg.setWindowTitle(_translate("buyer_info_dlg", "????????????"))
        self.l_buyer_info.setText(_translate("buyer_info_dlg", "??????????????????????????????"))
        self.l_area.setText(_translate("buyer_info_dlg", "????????????"))
        self.cb_buy_or_rent.setItemText(0, _translate("buyer_info_dlg", "??????"))
        self.cb_buy_or_rent.setItemText(1, _translate("buyer_info_dlg", "??????"))
        self.l_moremsg.setText(_translate("buyer_info_dlg", "??????"))
        self.label_6.setText(_translate("buyer_info_dlg", "        "))
        self.l_buy_or_rent.setText(_translate("buyer_info_dlg", "???/??????"))
        self.l_price.setText(_translate("buyer_info_dlg", "????????????"))
        self.label_7.setText(_translate("buyer_info_dlg", "    "))
        self.label_9.setText(_translate("buyer_info_dlg", " "))
