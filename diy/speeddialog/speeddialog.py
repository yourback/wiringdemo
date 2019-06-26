from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox

from diy.speeddialog.speeddialogui import Ui_Dialog


class SPEEDDialog(QDialog, Ui_Dialog):
    speed_confirm = pyqtSignal(int)

    def __init__(self, parent=None):
        super(SPEEDDialog, self).__init__(parent)
        self.setupUi(self)
        self.et_speed.setFocus()

    @pyqtSlot()
    def on_btn_avoid_cancel_clicked(self):
        self.close()

    @pyqtSlot()
    def on_btn_avoid_insert_clicked(self):
        val_speed = self.et_speed.text()
        if val_speed:
            self.speed_confirm.emit(int(val_speed))
            self.close()
        else:
            QMessageBox.information(self, '提示', '请填入速度量')

    def closeEvent(self, QCloseEvent):
        self.et_speed.clear()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    ui = SPEEDDialog()
    ui.show()
    sys.exit(app.exec_())
