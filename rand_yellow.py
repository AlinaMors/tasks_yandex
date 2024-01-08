import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor
import random


class CircleGenerator(QWidget):
    def __init__(self, parent=None):
        super(CircleGenerator, self).__init__(parent)
        self.setGeometry(100, 100, 800, 800)
        self.pushButton = QPushButton('Создать окружность', self)
        self.pushButton.setGeometry(10, 10, 150, 30)
        self.pushButton.clicked.connect(self.generate_circle)
        self.flag = False


    def generate_circle(self):
        self.flag = True
        self.size = random.randint(30, 100)
        self.x = random.randint(0, self.width() - self.size)
        self.y = random.randint(0, self.height() - self.size)
        self.color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter(self)
            qp.setBrush(self.color)
            qp.setPen(self.color)
            qp.drawEllipse(self.x, self.y, self.size, self.size)
            qp.end()


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.central_widget = CircleGenerator(self)
        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('Git и случайные окружности')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MyWindow()
    mainWindow.show()
    sys.exit(app.exec_())
