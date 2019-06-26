from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox

from diy.movedialog.movedialogui import Ui_Dialog


class MOVEDialog(QDialog, Ui_Dialog):
    move_confirm = pyqtSignal(bool, float, float, float)

    def __init__(self, parent=None):
        super(MOVEDialog, self).__init__(parent)
        self.setupUi(self)
        self.et_val_x.setFocus()

    @pyqtSlot()
    def on_btn_move_cancel_clicked(self):
        print('cancel')
        self.close()

    @pyqtSlot()
    def on_btn_move_insert_clicked(self):
        val_x = self.et_val_x.text()
        val_y = self.et_val_y.text()
        val_z = self.et_val_z.text()
        if val_x and val_y and val_z:
            self.move_confirm.emit(self.rb_absolutly.isChecked(), float(val_x), float(val_y),
                                   float(val_z))
            self.close()
        else:
            QMessageBox.information(self, '提示', '请填入x,y,z值')

    def closeEvent(self, QCloseEvent):
        self.rb_relatively.setChecked(True)
        self.et_val_x.clear()
        self.et_val_z.clear()
        self.et_val_y.clear()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    ui = MOVEDialog()
    ui.show()
    sys.exit(app.exec_())
