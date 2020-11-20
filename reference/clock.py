# - * - coding: utf8 - * -

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QTimer

import datetime # 時計を表示するために必要なので必ずimportしましょう。


class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'ステータスバー時計だよウィンドウ'
        self.width = 500
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(0, 0, self.width, self.height)
        self.show()

        timer = QTimer(self)
        timer.timeout.connect(self.getDateTime)
        timer.start(1000) # 1000ミリ秒

    def getDateTime(self):
        dt = datetime.datetime.today()
        dt_str = dt.strftime('%Y年%m月%d日 %H時%M分%S秒')
        self.statusBar().showMessage(
                'ステータスバーに時計が出たよ'
                + ' '
                + dt_str
                )


def main():
    app = QApplication(sys.argv)
    gui = MyWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()