import sys, sqlite3

from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QGridLayout, QPushButton, QLabel, QLineEdit, QTextEdit, QGridLayout, QInputDialog
from PyQt5.QtGui import QIcon, QPainter, QColor, QPen
from PyQt5.QtCore import Qt
import SqLite
import Candy
import ANI

class Example(QWidget):
    i=0
    def __init__(self):
        super().__init__()
        self.initUI()
        self.point = None


    def initUI(self):

        self.resize(400, 400)
        size = self.size()
        # Size of button based on screen sized
        btxsize = size.width() * 0.26
        btysize = 23
        # Window settings
        self.center()
        self.setWindowTitle('Anny')
        self.setWindowIcon(QIcon('anny.jpg'))
        # Buttons:
        #   closeButton
        btnclose = QPushButton('Close', self)
        btnclose.resize(btxsize, btysize)
        btnclose.move(size.width()-btxsize-29, size.height()-btysize-29)
        #   inputBox
        le = QLineEdit(self)
        le.resize(btxsize, btysize)
        le.move((size.width()/2)-(btxsize/2), (size.height()/2)-(btysize*2))
        #   reverseButton
        btnreverse = QPushButton('Reverse', self)
        btnreverse.resize(btxsize, btysize)
        btnreverse.move((size.width()/2)-(btxsize/2), (size.height()/2)-(btysize*2)+btysize+10)
        Example.btxsize1 = size.width() * 0.26
        Example.btysize1 = 23
        Example.rbcoorx =(size.width()/2)-(btxsize/2)
        Example.rbcoory = (size.height()/2)-(btysize*2)+btysize+10
        self.show()

    # Draw stuff
    def mousePressEvent(self, event):
        self.point = event.pos()
        xcor = event.x()
        ycor = event.y()
        print(xcor)
        print(ycor)
        SqLite.Data.litewrite(0, xcor, ycor)
        Example.i = Example.i + 1
        print(Example.i)
        # Вызов перерисовки виджета
        self.update()

    def VecotrLine(self, event):
        super().paintEvent(event)
        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()

    def drawLines(self, qp):
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        qp.setPen(pen)
        AnnyList = Candy.Anny.train(0,SqLite.Data.getxinputs(0),SqLite.Data.getyinputs(0),len(SqLite.Data.getxinputs(0))-1)
        qp.drawLine(Example.rbcoorx+Example.btxsize1/2, Example.rbcoory+Example.btysize1/2, AnnyList[0], AnnyList[1])

    def mouseReleaseEvent(self, event):
        self.point = None

    def paintEvent(self, event):
        super().paintEvent(event)

        # Если нет
        if not self.point:
            return
        # Рисовать будем на самом себе
        qp = QPainter(self)
        # Для рисования точки хватит setPen, но для других фигур (типо rect) понадобится setBrush
        qp.setPen(QPen(Qt.red, 5.0))
        if Example.i == 15:
            self.drawLines(qp)
            Example.i = 0
        # Рисование точки
        qp.drawPoint(self.point)



    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())