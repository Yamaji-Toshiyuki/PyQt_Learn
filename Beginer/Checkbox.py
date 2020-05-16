import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sip

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # 1つ目のチェックボックス
        self.upper = QCheckBox('大文字', self)
        self.upper.move(100, 30)
        self.upper.stateChanged.connect(self.uppercase)

        #横のレイアウト
        self.horizon = QHBoxLayout()
        #縦のレイアウト
        self.vertical = QVBoxLayout()

        self.horizon.addLayout(self.vertical)
        self.setLayout(self.horizon)

        self.setGeometry(300, 50, 400, 350)
        self.setWindowTitle('QCheckBox')

    def uppercase(self):
        if(self.upper.isChecked()):
            self.upper_a = QCheckBox('A',self)
            self.vertical.addWidget(self.upper_a)

            self.upper_b = QCheckBox('B',self)
            self.vertical.addWidget(self.upper_b)
        else:
            self.vertical.removeWidget(self.upper_a)
            self.vertical.removeWidget(self.upper_b)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())