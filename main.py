import sys
from PyQt6.QtCore import Qt, QRectF, QPointF
from math import sin, cos, pi
from PyQt6.QtWidgets import QWidget, QApplication
from random import randint as RI
from PyQt6.QtGui import QPainter, QColor, QPolygonF


class Suprematism(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.STATUS = 0
        self.coords = (None, None)
        self.flag = False
        self.setMouseTracking(True)

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Супрематизм')

    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw_flag(self.qp)
            self.qp.end()
        self.flag = False

    def draw_flag(self, qp):
        D = RI(20, 100)
        r, g, b = RI(0, 255), RI(0, 255), RI(0, 255)
        qp.setBrush(QColor(r, g, b))
        x, y = self.coords
        if self.STATUS == 1:
            qp.drawEllipse(QPointF(x, y), D, D)

        if self.STATUS == 2:
            x, y = x - D / 2, y - D / 2
            qp.drawRect(QRectF(x, y, D, D))

        if self.STATUS == 3:
            coords = QPolygonF([QPointF(x, y - D),
                                QPointF(x + cos(7 * pi / 6) * D,
                                        y - sin(7 * pi / 6) * D),
                                QPointF(x + cos(11 * pi / 6) * D,
                                        y - sin(11 * pi / 6) * D)])
            self.qp.drawPolygon(coords)
        self.STATUS = 0

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Space:
            self.STATUS = 3
            self.drawf()

    def mouseMoveEvent(self, event):
        self.coords = event.pos().x(), event.pos().y()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.STATUS = 1
            self.drawf()
        elif event.button() == Qt.MouseButton.RightButton:
            self.STATUS = 2
            self.drawf()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec())