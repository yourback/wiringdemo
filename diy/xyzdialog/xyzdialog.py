from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QMessageBox, QApplication, QDialog

from diy.xyzdialog.xyzdialogui import Ui_Dialog


class XYZDialog(QDialog, Ui_Dialog):
    xyz_confirm = pyqtSignal(int, int)

    def __init__(self, parent=None):
        super(XYZDialog, self).__init__(parent)
        self.setupUi(self)
        self.et_xyz_base.setFocus()

    @pyqtSlot()
    def on_btn_xyz_cancel_clicked(self):
        print('cancel')
        self.close()

    @pyqtSlot()
    def on_btn_xyz_insert_clicked(self):
        val_base = self.et_xyz_base.text()
        val_tool = self.et_xyz_tool.text()
        if val_base or val_tool:
            self.xyz_confirm.emit(int(val_base) if val_base else 0, int(val_tool) if val_tool else 0)
            self.close()
        else:
            QMessageBox.information(self, '提示', '请填入基础坐标系或者工具坐标系值')

    def closeEvent(self, QCloseEvent):
        self.et_xyz_base.clear()
        self.et_xyz_tool.clear()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    ui = XYZDialog()
    ui.show()
    sys.exit(app.exec_())
