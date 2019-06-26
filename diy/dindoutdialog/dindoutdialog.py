from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QMessageBox, QApplication, QDialog

from diy.dindoutdialog.dindoutdialogui import Ui_Dialog


class DinDoutDialog(QDialog, Ui_Dialog):
    dindout_confirm = pyqtSignal(bool, float, str)

    def __init__(self, parent=None):
        super(DinDoutDialog, self).__init__(parent)
        self.setupUi(self)
        self.et_val_port.setFocus()

    @pyqtSlot()
    def on_btn_d_cancel_clicked(self):
        print('cancel')
        self.close()

    @pyqtSlot()
    def on_btn_d_insert_clicked(self):
        val_port = self.et_val_port.text()
        val_status = self.cb_onoff.currentText()
        if val_port and val_status:
            self.dindout_confirm.emit(self.rb_din.isChecked(), int(val_port), val_status)
            self.close()
        else:
            QMessageBox.information(self, '提示', '请填入端口号并选择状态')

    def closeEvent(self, QCloseEvent):
        self.rb_din.setChecked(True)
        self.et_val_port.clear()
        self.cb_onoff.setCurrentIndex(0)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    ui = DinDoutDialog()
    ui.show()
    sys.exit(app.exec_())
