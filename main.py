from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout
from PyQt5.QtGui import QPainter, QColor, QPixmap, QPen, QBrush
from random import randrange
from Ui import Ui_MainWindow
import sys


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.draw_circle)
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap(1200, 800))
        self.label.setStyleSheet('background-color: rgb(255, 255, 255);')
        self.lout = QGridLayout(self.centralWidget())
        self.lout.addWidget(self.pushButton, 0, 0)
        self.lout.addWidget(self.label, 1, 0)

    def draw_circle(self):
        x, y = randrange(0, 1000), randrange(0, 800)
        w = randrange(500)
        self.qp = QPainter()
        self.qp.begin(self.label.pixmap())
        self.qp.setPen(QPen(QColor(randrange(256), randrange(256), randrange(256)), 6))
        self.qp.drawEllipse(x, y, w, w)
        self.qp.end()
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = Main()
    m.show()
    sys.exit(app.exec())
