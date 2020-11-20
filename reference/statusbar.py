# - * - coding: utf8 - * -

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication


class MyWindow(QMainWindow): # QMainWindowクラスを使用します。

    def __init__(self):
        super().__init__()
        self.title = 'QMainWindowウィンドウだよ'
        self.width = 500
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(0, 0, self.width, self.height)
        self.statusBar().showMessage('ここがステータスバーだよ')
        self.show()


def main():
    app = QApplication(sys.argv)
    gui = MyWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()