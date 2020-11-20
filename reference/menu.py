# - * - coding: utf8 - * -

import sys

# from PyQt5.QtWidgets import QMainWindow, QApplication, Qaction, qApp
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'メニューバーがあるウィンドウだよウィンドウ'
        self.width = 500
        self.height = 400
        self.initUI()

    def initUI(self):

        ### メニューバーアクションの定義 ###
        exitAction = QAction('&終了', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('GUI画面を閉じるよ')
        exitAction.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&ファイル')
        fileMenu.addAction(exitAction) # fileMenuにアクションを追加します。

        self.setWindowTitle(self.title)
        self.setGeometry(0, 0, self.width, self.height)

        self.statusBar()

        self.show()

def main():
    app = QApplication(sys.argv)
    gui = MyWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()