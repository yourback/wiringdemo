# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dindoutdialogui.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(274, 184)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(20, 0, 20, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.rb_din = QtWidgets.QRadioButton(Dialog)
        self.rb_din.setChecked(True)
        self.rb_din.setObjectName("rb_din")
        self.horizontalLayout_2.addWidget(self.rb_din)
        self.rb_dout = QtWidgets.QRadioButton(Dialog)
        self.rb_dout.setObjectName("rb_dout")
        self.horizontalLayout_2.addWidget(self.rb_dout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(50, -1, 50, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.et_val_port = QtWidgets.QLineEdit(Dialog)
        self.et_val_port.setObjectName("et_val_port")
        self.horizontalLayout_6.addWidget(self.et_val_port)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(50, -1, 50, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.cb_onoff = QtWidgets.QComboBox(Dialog)
        self.cb_onoff.setObjectName("cb_onoff")
        self.cb_onoff.addItem("")
        self.cb_onoff.addItem("")
        self.horizontalLayout_4.addWidget(self.cb_onoff)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_d_insert = QtWidgets.QPushButton(Dialog)
        self.btn_d_insert.setObjectName("btn_d_insert")
        self.horizontalLayout.addWidget(self.btn_d_insert)
        self.btn_d_cancel = QtWidgets.QPushButton(Dialog)
        self.btn_d_cancel.setObjectName("btn_d_cancel")
        self.horizontalLayout.addWidget(self.btn_d_cancel)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_2.setStretch(0, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "设置串口状态"))
        self.rb_din.setText(_translate("Dialog", "D_in"))
        self.rb_dout.setText(_translate("Dialog", "D_out"))
        self.label_3.setText(_translate("Dialog", "端口号："))
        self.label.setText(_translate("Dialog", "状态："))
        self.cb_onoff.setItemText(0, _translate("Dialog", "ON"))
        self.cb_onoff.setItemText(1, _translate("Dialog", "OFF"))
        self.btn_d_insert.setText(_translate("Dialog", "插入"))
        self.btn_d_cancel.setText(_translate("Dialog", "取消"))


