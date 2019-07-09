import os

from PyQt5.QtWidgets import QFileDialog, QMessageBox


# 新建程序
def save_program(win):
    f_name, _ = QFileDialog.getSaveFileName(win, '新建程序', '.', '*.PRG')
    context = ''
    if f_name:
        with open(f_name, 'w') as f:
            context = '''PROGRAM
WITH ROBOT
ATTACH ROBOT
ATTACH EXT_AXES
`start

`end
DETACH ROBOT
DETACH EXT_AXES
END WITH
END PROGRAM'''
            f.write(context)
        return f_name, context
    return '', ''


# 新建子程序
def save_lib(win):
    f_name, _ = QFileDialog.getSaveFileName(win, '新建程序', '.', '*.LIB')
    context = ''
    if f_name:
        with open(f_name, 'w') as f:
            context = '''PUBLIC SUB %s
`start

`end
END SUB''' % os.path.splitext(os.path.split(f.name)[1])[0]
            f.write(context)
        return f_name, context
    return '', ''


# 新建加密程序
def save_jiami(win):
    files = get_all_PRGLIB_file()
    if files:
        f_name, _ = QFileDialog.getSaveFileName(win, '新建加密程序', '.', '*.PRG')
        if f_name:
            with open(f_name, 'w') as f:
                f.write('PROGRAM\n')
                # get all LIB or PRG File name
                for n in files:
                    f.write('?ENCRYPTFILE("%s")\n' % n)
                f.write('END PROGRAM')

            QMessageBox.information(win, '加密成功', '加密文件个数：%s' % len(files))

    else:
        QMessageBox.information(win, '提示', '当前文件夹下没有需要加密的文件')


def get_all_PRGLIB_file():
    result_list = []
    for name in os.listdir('.'):
        if name.endswith('.PRG') or name.endswith('.LIB'):
            result_list.append(name)
    return result_list


# 打开文件
def open_file(win):
    filename, _ = QFileDialog.getOpenFileName(win, '打开文件', filter='*.PRG;;*.LIB', directory='.')
    if filename:
        print('打开文件名称：%s' % filename)
        file_content = ''
        try:
            with open(filename, 'r',encoding='utf-8') as f:
                file_content = f.read()

            return filename, file_content
        except Exception as e:
            print('错误：%s' % e)
    else:
        return '', ''


# 选择子程序
def choose_file(win):
    filename, _ = QFileDialog.getOpenFileName(win, '打开文件', filter='*.LIB', directory='.')
    if filename:
        return '%s()' % os.path.splitext(os.path.split(filename)[1])[0]
    else:
        return ''
