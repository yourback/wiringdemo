# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'valdialogui.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(274, 107)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(50, -1, 50, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.et_val_name = QtWidgets.QLineEdit(Dialog)
        self.et_val_name.setObjectName("et_val_name")
        self.horizontalLayout_3.addWidget(self.et_val_name)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(50, -1, 50, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.et_val_value = QtWidgets.QLineEdit(Dialog)
        self.et_val_value.setObjectName("et_val_value")
        self.horizontalLayout_2.addWidget(self.et_val_value)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_val_insert = QtWidgets.QPushButton(Dialog)
        self.btn_val_insert.setObjectName("btn_val_insert")
        self.horizontalLayout.addWidget(self.btn_val_insert)
        self.btn_val_cancel = QtWidgets.QPushButton(Dialog)
        self.btn_val_cancel.setObjectName("btn_val_cancel")
        self.horizontalLayout.addWidget(self.btn_val_cancel)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "添加变量"))
        self.label_2.setText(_translate("Dialog", "变量名："))
        self.label.setText(_translate("Dialog", "初始值："))
        self.btn_val_insert.setText(_translate("Dialog", "插入"))
        self.btn_val_cancel.setText(_translate("Dialog", "取消"))


