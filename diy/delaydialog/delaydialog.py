from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QMessageBox, QApplication, QDialog

from diy.delaydialog.delaydialogui import Ui_Dialog


class DELAYDialog(QDialog, Ui_Dialog):
    delay_confirm = pyqtSignal(int)

    def __init__(self, parent=None):
        super(DELAYDialog, self).__init__(parent)
        self.setupUi(self)
        self.et_delay_s.setFocus()

    @pyqtSlot()
    def on_btn_delay_cancel_clicked(self):
        self.close()

    @pyqtSlot()
    def on_btn_delay_insert_clicked(self):
        val_s = self.et_delay_s.text()
        if val_s:
            self.delay_confirm.emit(int(val_s))
            self.close()
        else:
            QMessageBox.information(self, '提示', '请填入非零延时秒数')

    def closeEvent(self, QCloseEvent):
        self.et_delay_s.clear()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    ui = DELAYDialog()
    ui.show()
    sys.exit(app.exec_())
