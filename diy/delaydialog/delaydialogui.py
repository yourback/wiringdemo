# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delaydialogui.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(274, 116)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(50, -1, 50, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.et_delay_s = QtWidgets.QLineEdit(Dialog)
        self.et_delay_s.setObjectName("et_delay_s")
        self.horizontalLayout_6.addWidget(self.et_delay_s)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_delay_insert = QtWidgets.QPushButton(Dialog)
        self.btn_delay_insert.setObjectName("btn_delay_insert")
        self.horizontalLayout.addWidget(self.btn_delay_insert)
        self.btn_delay_cancel = QtWidgets.QPushButton(Dialog)
        self.btn_delay_cancel.setObjectName("btn_delay_cancel")
        self.horizontalLayout.addWidget(self.btn_delay_cancel)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_2.setStretch(0, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "设置坐标系"))
        self.label_3.setText(_translate("Dialog", "延时："))
        self.label.setText(_translate("Dialog", "毫秒"))
        self.btn_delay_insert.setText(_translate("Dialog", "插入"))
        self.btn_delay_cancel.setText(_translate("Dialog", "取消"))


