from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QMessageBox

from diy.aboutdialog.amdialog import AMDialog
from diy.delaydialog.delaydialog import DELAYDialog
from diy.dindoutdialog.dindoutdialog import DinDoutDialog
from diy.movedialog.movedialog import MOVEDialog
from diy.speeddialog.speeddialog import SPEEDDialog
from diy.valdialog.valdialog import VALDialog
from diy.xyzdialog.xyzdialog import XYZDialog
from settings import if_block, move_block, app_name, speed_block, xyz_base_block, xyz_tool_block, din_block, dout_block, \
    delay_block, val_block
from ui.mianwin import Ui_MainWindow
from util.fileutil import save_program, save_lib, save_jiami, open_file, choose_file


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.init_dialog()
        self.localfile_action = QAction(self)
        self.current_file_name = ''
        self.setupUi(self)
        self.setWindowTitle(app_name)
        self.init_listener()

    def init_listener(self):
        # current program name
        self.program_edit.setEnabled(False)
        # update log
        self.about.clicked.connect(self.about_click)

        self.localfile_action.setCheckable(False)
        self.localfile_action.setObjectName('localFileAction')
        self.localfile_action.triggered.connect(self.on_open_menu_triggered)
        self.localfile_action.setText('打开')
        self.menubar.addAction(self.localfile_action)

    def init_dialog(self):
        # 行进
        self.move_menu_dialog = MOVEDialog()
        self.move_menu_dialog.move_confirm.connect(self.move_menu_confirm)
        # 坐标系
        self.xyz_menu_dialog = XYZDialog()
        self.xyz_menu_dialog.xyz_confirm.connect(self.xyz_menu_confirm)
        # 速度
        self.speed_menu_dialog = SPEEDDialog()
        self.speed_menu_dialog.speed_confirm.connect(self.speed_menu_confirm)
        # 输入输出
        self.dindiout_menu_dialog = DinDoutDialog()
        self.dindiout_menu_dialog.dindout_confirm.connect(self.dindiout_menu_confirm)
        # 延时
        self.delay_menu_dialog = DELAYDialog()
        self.delay_menu_dialog.delay_confirm.connect(self.delay_menu_confirm)
        # 变量
        self.val_menu_dialog = VALDialog()
        self.val_menu_dialog.val_confirm.connect(self.val_menu_confirm)

    # 新建程序
    @pyqtSlot()
    def on_program_menu_triggered(self):
        print('program_menu')
        filename, filecontent = save_program(self)
        if filename:
            self.program_edit.setText(filecontent)
            self.current_file_name = filename
            self.set_program_edit_enable(True)

    # 新建子程序
    @pyqtSlot()
    def on_lib_menu_triggered(self):
        print('lib_menu')
        filename, filecontent = save_lib(self)
        if filename:
            self.program_edit.setText(filecontent)
            self.current_file_name = filename
            self.set_program_edit_enable(True)

    # 新建加密程序
    @pyqtSlot()
    def on_jiami_menu_triggered(self):
        print('jiami_menu')
        save_jiami(self)

    # 打开文件
    def on_open_menu_triggered(self):
        print('open_menu')
        filename, filecontent = open_file(self)
        print('文件名称：%s' % filename)
        print('文件内容：%s' % filecontent)
        if filename:
            self.current_file_name = filename
            self.program_edit.setText(filecontent)
            self.set_program_edit_enable(True)

    # edit可用并移动光标到'`start'之后
    def set_program_edit_enable(self, bool):
        self.insert.setEnabled(bool)
        if bool:
            self.program_edit.setEnabled(True)
            corsor_move = self.program_edit.toPlainText().find('`start') + '`start'.__len__() + 1
            self.set_cursor_position(corsor_move)
        else:
            self.program_edit.setEnabled(False)

    # 设置self.program_edit光标位置
    def set_cursor_position(self, line_position):
        for _ in range(line_position):
            self.program_edit.moveCursor(19)

    # 文档内容改变
    @pyqtSlot()
    def on_program_edit_textChanged(self):
        # print('内容改变')
        if self.current_file_name:
            with open(self.current_file_name, 'w+') as f:
                f.write(self.program_edit.toPlainText())

    # 添加变量
    @pyqtSlot()
    def on_val_menu_triggered(self):
        print('val_menu')
        self.val_menu_dialog.exec()

    # 添加变量生效
    def val_menu_confirm(self, val_name, val_value):
        # 先看是什么文件
        print(self.current_file_name)
        self.program_edit.moveCursor(1)
        if self.current_file_name.endswith('PRG'):
            print('插入变量到程序')
            str = val_block % (val_name, val_value)
            # 光标移动到‘PROGRAM之后’
            corsor_move = self.program_edit.toPlainText().find('PROGRAM') + 'PROGRAM'.__len__() + 1
            print(corsor_move)
            self.set_cursor_position(corsor_move)
            self.program_edit.textCursor().insertText(str)
        elif self.current_file_name.endswith('LIB'):
            print('插入变量到子程序')
            str = val_block % (val_name, val_value)
            # 光标移动到最前端
            self.program_edit.textCursor().insertText(str)
        else:
            QMessageBox.information(self, '错误', '当前文件出错')

    # 添加ifelse逻辑
    @pyqtSlot()
    def on_if_menu_triggered(self):
        self.program_edit.textCursor().insertText(if_block)

    # 行进操作
    @pyqtSlot()
    def on_move_menu_2_triggered(self):
        self.move_menu_dialog.exec()

    # 行进操作生效
    def move_menu_confirm(self, b, f1, f2, f3):
        self.program_edit.textCursor().insertText(move_block % (f1, f2, f3, 1 if b else 0))

    # # 避障操作删除
    # @pyqtSlot()
    # def on_avoid_menu_triggered(self):
    #     print('avoid_menu')

    # 速度
    @pyqtSlot()
    def on_speed_menu_triggered(self):
        print('speed_menu')
        self.speed_menu_dialog.exec()

    # 速度设置生效
    def speed_menu_confirm(self, int_speed):
        self.program_edit.textCursor().insertText(speed_block % int(int_speed))

    # 坐标系
    @pyqtSlot()
    def on_xyz_menu_triggered(self):
        print('xyz_menu')
        self.xyz_menu_dialog.exec()

    # 坐标系生效
    def xyz_menu_confirm(self, int_base, int_tool):
        if int_base:
            self.program_edit.textCursor().insertText(xyz_base_block % int(int_base))

        if int_tool:
            self.program_edit.textCursor().insertText(xyz_tool_block % int(int_tool))

    # 输入输出
    @pyqtSlot()
    def on_dindout_menu_triggered(self):
        print('din_menu')
        self.dindiout_menu_dialog.exec()

    # 输入输出生效
    def dindiout_menu_confirm(self, direction, port_num, status):
        if direction:
            self.program_edit.textCursor().insertText(din_block % (int(port_num), status))
        else:
            self.program_edit.textCursor().insertText(dout_block % (int(port_num), status))

    # 延时
    @pyqtSlot()
    def on_delay_menu_triggered(self):
        print('delay_menu')
        self.delay_menu_dialog.exec()

    # 延时生效
    def delay_menu_confirm(self, second):
        print('延时second')
        self.program_edit.textCursor().insertText(delay_block % second)

    # 引用
    @pyqtSlot()
    def on_call_menu_triggered(self):
        lib_name = choose_file(self)
        if lib_name:
            self.program_edit.textCursor().insertText(lib_name)

    def about_click(self):
        '''查看升级日志'''
        ui = AMDialog()
        ui.exec()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
