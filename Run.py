# -*- coding:utf-8 -*-
# @Time : 2022/5/27 14:56
# @Author : 西~南~北
# @File : Run.py
# @Software: PyCharm
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from LPRGUI import Ui_MainWindow


class LPR(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(LPR, self).__init__()
        self.setupUi(self)


def LPR_plus():
    app = QApplication(sys.argv)
    ex = LPR()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    LPR_plus()
