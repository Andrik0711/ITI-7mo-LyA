import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class StackWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.current_index = -1
        self.animation = None
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('Stack Animation')

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(QPen(Qt.black, 2, Qt.SolidLine))

        # Draw stack elements
        for i, element in enumerate(self.stack):
            if i == self.current_index:
                # Draw moving element
                qp.setBrush(QBrush(Qt.red))
            else:
                qp.setBrush(QBrush(Qt.blue))
            qp.drawEllipse(50, 50 + 50*i, 50, 50)

        qp.end()

    def push(self):
        self.stack.append(0)
        self.current_index += 1
        self.animate()

    def pop(self):
        if not self.stack:
            return
        self.current_index -= 1
        self.animate()

    def animate(self):
        if self.animation is not None:
            self.animation.stop()
        self.animation = QPropertyAnimation(self, b"dummy")
        self.animation.setDuration(1000)
        self.animation.setEasingCurve(QEasingCurve.InOutCubic)
        self.animation.start()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.push()
        elif event.button() == Qt.RightButton:
            self.pop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    stack_widget = StackWidget()
    stack_widget.show()
    sys.exit(app.exec_())
