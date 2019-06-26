from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox

from diy.valdialog.valdialogui import Ui_Dialog


class VALDialog(QDialog, Ui_Dialog):
    val_confirm = pyqtSignal(str, int)

    def __init__(self, parent=None):
        super(VALDialog, self).__init__(parent)
        self.setupUi(self)

        self.et_val_name.setPlaceholderText('str')
        self.et_val_value.setPlaceholderText('int')
        self.et_val_name.setFocus()

    @pyqtSlot()
    def on_btn_val_cancel_clicked(self):
        self.close()

    @pyqtSlot()
    def on_btn_val_insert_clicked(self):
        val_name = self.et_val_name.text()
        val_value = self.et_val_value.text()
        if val_name and val_value:
            self.val_confirm.emit(val_name, int(val_value))
            self.close()
        else:
            QMessageBox.information(self, '提示', '请填入变量与其初始值')

    def closeEvent(self, QCloseEvent):
        self.et_val_name.clear()
        self.et_val_value.clear()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    ui = VALDialog()
    ui.show()
    sys.exit(app.exec_())
