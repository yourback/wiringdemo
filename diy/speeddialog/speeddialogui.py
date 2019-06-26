# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'speeddialogui.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(274, 82)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(50, -1, 50, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.et_speed = QtWidgets.QLineEdit(Dialog)
        self.et_speed.setObjectName("et_speed")
        self.horizontalLayout_2.addWidget(self.et_speed)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_avoid_insert = QtWidgets.QPushButton(Dialog)
        self.btn_avoid_insert.setObjectName("btn_avoid_insert")
        self.horizontalLayout.addWidget(self.btn_avoid_insert)
        self.btn_avoid_cancel = QtWidgets.QPushButton(Dialog)
        self.btn_avoid_cancel.setObjectName("btn_avoid_cancel")
        self.horizontalLayout.addWidget(self.btn_avoid_cancel)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_2.setStretch(0, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "速度调节"))
        self.label.setText(_translate("Dialog", "速度量："))
        self.btn_avoid_insert.setText(_translate("Dialog", "插入"))
        self.btn_avoid_cancel.setText(_translate("Dialog", "取消"))


