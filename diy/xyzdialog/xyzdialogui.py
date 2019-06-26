# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xyzdialogui.ui'
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
        self.et_xyz_base = QtWidgets.QLineEdit(Dialog)
        self.et_xyz_base.setObjectName("et_xyz_base")
        self.horizontalLayout_6.addWidget(self.et_xyz_base)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(50, -1, 50, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.et_xyz_tool = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.et_xyz_tool.sizePolicy().hasHeightForWidth())
        self.et_xyz_tool.setSizePolicy(sizePolicy)
        self.et_xyz_tool.setObjectName("et_xyz_tool")
        self.horizontalLayout_4.addWidget(self.et_xyz_tool)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_xyz_insert = QtWidgets.QPushButton(Dialog)
        self.btn_xyz_insert.setObjectName("btn_xyz_insert")
        self.horizontalLayout.addWidget(self.btn_xyz_insert)
        self.btn_xyz_cancel = QtWidgets.QPushButton(Dialog)
        self.btn_xyz_cancel.setObjectName("btn_xyz_cancel")
        self.horizontalLayout.addWidget(self.btn_xyz_cancel)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_2.setStretch(0, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "设置坐标系"))
        self.label_3.setText(_translate("Dialog", "基础座标系："))
        self.label.setText(_translate("Dialog", "工具坐标系："))
        self.btn_xyz_insert.setText(_translate("Dialog", "插入"))
        self.btn_xyz_cancel.setText(_translate("Dialog", "取消"))


