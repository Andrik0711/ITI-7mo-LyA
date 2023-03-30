import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from collections import deque


class ArrayStack(QWidget):
    def __init__(self):
        super().__init__()
        self.stack = []

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(QColor(qRgb(231, 95, 95)), 2, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.white, Qt.SolidPattern))
        width = 50
        height = 30
        x = 50
        y = 50

        for i, item in enumerate(self.stack):
            rect = QRect(x, y, width, height)
            painter.drawRect(rect)
            painter.drawText(rect, Qt.AlignCenter, str(item))
            x += width + 10

        painter.end()

    def push(self, item):
        self.stack.append(item)
        self.update()

    def pop(self):
        if len(self.stack) > 0:
            self.stack.pop()
            self.update()


class FastArrayStack(QWidget):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.top = -1

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(QColor(qRgb(231, 95, 95)), 2, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.white, Qt.SolidPattern))
        width = 50
        height = 30
        x = 50
        y = 50

        for i, item in enumerate(self.stack):
            rect = QRect(x, y, width, height)
            painter.drawRect(rect)
            painter.drawText(rect, Qt.AlignCenter, str(item))
            x += width + 10

        painter.end()

    def push(self, item):
        self.top += 1
        if self.top < len(self.stack):
            self.stack[self.top] = item
        else:
            self.stack.append(item)
        self.update()

    def pop(self):
        if len(self.stack) > 0:
            self.stack.pop()
            self.top -= 1
            self.update()


class ArrayDeque(QWidget):
    def __init__(self):
        super().__init__()
        self.array = [None] * 2
        self.front = -1
        self.rear = -1

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(QColor(qRgb(231, 95, 95)), 2, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.white, Qt.SolidPattern))
        width = 50
        height = 30
        x = 50
        y = 50

        for i, item in enumerate(self.array):
            rect = QRect(x, y, width, height)
            painter.drawRect(rect)
            painter.drawText(rect, Qt.AlignCenter, str(item))
            x += width + 10

        painter.end()

    def push_front(self, item):
        if self.front == 0:
            self.array = [None] * len(self.array) + self.array
            self.front += len(self.array) // 2
            self.rear += len(self.array) // 2
        elif self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            self.front -= 1
        self.array[self.front] = item
        self.update()

    def push_back(self, item):
        if self.rear == len(self.array) - 1:
            self.array += [None] * len(self.array)
        self.rear += 1
        self.array[self.rear] = item
        if self.front == -1:
            self.front = 0
        self.update()

    def pop_front(self):
        if self.front == -1:
            return
        item = self.array[self.front]
        self.array[self.front] = None
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front += 1
        self.update()
        return item

    def pop_back(self):
        if self.rear == -1:
            return
        item = self.array[self.rear]
        self.array[self.rear] = None
        self.rear -= 1
        if self.rear < self.front:
            self.front = -1
            self.rear = -1
        self.update()
        return item


class ArrayQueue(QWidget):
    def __init__(self):
        super().__init__()
        self.array = [None] * 2
        self.front = -1
        self.rear = -1

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(QColor(qRgb(231, 95, 95)), 2, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.white, Qt.SolidPattern))
        width = 50
        height = 30
        x = 50
        y = 50

        # Iterar sobre los elementos de la cola
        for i in range(self.front, self.rear + 1):
            item = self.array[i]
            rect = QRect(x, y, width, height)
            painter.drawRect(rect)
            painter.drawText(rect, Qt.AlignCenter, str(item))
            x += width + 10

        painter.end()

    def enqueue(self, item):
        if self.rear == len(self.array) - 1:
            self.array += [None] * len(self.array)
        self.rear += 1
        self.array[self.rear] = item
        if self.front == -1:
            self.front = 0
        self.update()

    def dequeue(self):
        if self.front == -1:
            return
        item = self.array[self.front]
        self.array[self.front] = None
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front += 1
        self.update()
        return item


class DualArrayDeque(QWidget):
    def __init__(self):
        super().__init__()
        self.front = deque()
        self.rear = deque()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(QColor(qRgb(231, 95, 95)), 2, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.white, Qt.SolidPattern))
        width = 50
        height = 30
        x = 50
        y = 50

        # Iterar sobre los elementos de la deque
        for i, item in enumerate(self.front + self.rear):
            rect = QRect(x, y, width, height)
            painter.drawRect(rect)
            painter.drawText(rect, Qt.AlignCenter, str(item))
            x += width + 10

            # Dibujar una línea vertical para separar las mitades
            if i == len(self.front) - 1:
                x += 10
                painter.drawLine(QPoint(x, y - 5), QPoint(x, y + height + 5))
                x += 10

        painter.end()

    def add_front(self, item):
        self.front.appendleft(item)
        self.update()

    def remove_front(self):
        if self.front:
            item = self.front.popleft()
            self.update()
            return item

    def add_rear(self, item):
        self.rear.append(item)
        self.update()

    def remove_rear(self):
        if self.rear:
            item = self.rear.pop()
            self.update()
            return item


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 290, 100)
        self.setWindowTitle('Menu de opciones')
        self.initUi()

    def initUi(self):
        # Creamos los botones y los conectamos con sus respectivos metodos de data structure
        self.buttonAS = QPushButton('ArrayStack', self)
        self.buttonAS.clicked.connect(self.open_window_array_stack)

        self.buttonFAS = QPushButton('FastArrayStack', self)
        self.buttonFAS.clicked.connect(self.open_window_fast_array_stack)

        self.buttonAD = QPushButton('ArrayDeque', self)
        self.buttonAD.clicked.connect(self.open_window_array_deque)

        self.buttonAQ = QPushButton('ArrayQueue', self)
        self.buttonAQ.clicked.connect(self.open_window_array_queue)

        self.buttonDAD = QPushButton('DualArrayDeque', self)
        self.buttonDAD.clicked.connect(self.open_window_dual_array_deque)

        self.buttonRAS = QPushButton('RootishArrayStack', self)
        self.buttonRAS.clicked.connect(self.open_window_rootish_array_stack)

        # centramos los botones en el menu principla
        self.center_buttons([self.buttonAS, self.buttonFAS, self.buttonAD,
                            self.buttonAQ, self.buttonDAD, self.buttonRAS])

    # generamos las ventanas de los botones
    def open_window_array_stack(self):
        layout = QVBoxLayout()
        stack_view = ArrayStack()
        push_button = QPushButton('Push')
        pop_button = QPushButton('Pop')

        def push_item():
            item, ok = QInputDialog.getText(window, 'Push', 'Enter item:')
            if ok:
                stack_view.push(item)

        def pop_item():
            stack_view.pop()

        push_button.clicked.connect(push_item)
        pop_button.clicked.connect(pop_item)

        layout.addWidget(stack_view)
        layout.addWidget(push_button)
        layout.addWidget(pop_button)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(push_button)
        hbox1.addWidget(pop_button)

        vbox1 = QVBoxLayout()
        vbox1.addLayout(hbox1)

        self.window_AS = QWidget()
        self.window_AS.setWindowTitle('ArrayStack window')
        self.window_AS.setGeometry(500, 500, 500, 500)
        self.window_AS.setLayout(layout)
        self.window_AS.show()

    def open_window_fast_array_stack(self):
        layout = QVBoxLayout()
        stack_view = FastArrayStack()
        push_button = QPushButton('Push')
        pop_button = QPushButton('Pop')

        def push_item():
            item, ok = QInputDialog.getText(window, 'Push', 'Enter item:')
            if ok:
                stack_view.push(item)

        def pop_item():
            stack_view.pop()

        push_button.clicked.connect(push_item)
        pop_button.clicked.connect(pop_item)

        layout.addWidget(stack_view)
        layout.addWidget(push_button)
        layout.addWidget(pop_button)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(push_button)
        hbox1.addWidget(pop_button)

        vbox1 = QVBoxLayout()
        vbox1.addLayout(hbox1)

        self.window_FAS = QWidget()
        self.window_FAS.setWindowTitle('FastArrayStack window')
        self.window_FAS.setGeometry(500, 500, 500, 500)
        self.window_FAS.setLayout(layout)
        self.window_FAS.show()

    def open_window_array_deque(self):
        layout = QVBoxLayout()
        stack_view = ArrayDeque()
        push_button_1 = QPushButton('Push Front')
        pop_button_1 = QPushButton('Pop Front')
        push_button_2 = QPushButton('Push Back')
        pop_button_2 = QPushButton('Pop Back')

        def push_item():
            item, ok = QInputDialog.getText(window, 'Push', 'Enter item:')
            if ok:
                stack_view.push_front(item)

        def pop_item():
            stack_view.pop_front()

        def push_item_2():
            item, ok = QInputDialog.getText(window, 'Push', 'Enter item:')
            if ok:
                stack_view.push_back(item)

        def pop_item_2():
            stack_view.pop_back()

        push_button_1.clicked.connect(push_item)
        pop_button_1.clicked.connect(pop_item)
        push_button_2.clicked.connect(push_item_2)
        pop_button_2.clicked.connect(pop_item_2)

        layout.addWidget(stack_view)
        layout.addWidget(push_button_1)
        layout.addWidget(pop_button_1)
        layout.addWidget(push_button_2)
        layout.addWidget(pop_button_2)

        self.window_AD = QWidget()
        self.window_AD.setWindowTitle('ArrayDeque window')
        self.window_AD.setGeometry(500, 500, 500, 500)
        self.window_AD.setLayout(layout)
        self.window_AD.show()

    def open_window_array_queue(self):
        layout = QVBoxLayout()
        queue_view = ArrayQueue()
        enqueue_button = QPushButton('Enqueue')
        dequeue_button = QPushButton('Dequeue')

        def enqueue_item():
            item, ok = QInputDialog.getText(window, 'Enqueue', 'Enter item:')
            if ok:
                queue_view.enqueue(item)

        def dequeue_item():
            queue_view.dequeue()

        enqueue_button.clicked.connect(enqueue_item)
        dequeue_button.clicked.connect(dequeue_item)

        layout.addWidget(queue_view)
        layout.addWidget(enqueue_button)
        layout.addWidget(dequeue_button)
        self.window_AQ = QWidget()
        self.window_AQ.setWindowTitle('ArrayQueue window')
        self.window_AQ.setGeometry(500, 500, 500, 500)
        self.window_AQ.setLayout(layout)
        self.window_AQ.show()

    def open_window_dual_array_deque(self):
        layout = QVBoxLayout()
        deque_view = DualArrayDeque()
        add_front_button = QPushButton('Add to front')
        remove_front_button = QPushButton('Remove from front')
        add_rear_button = QPushButton('Add to rear')
        remove_rear_button = QPushButton('Remove from rear')

        def add_front_item():
            item, ok = QInputDialog.getText(
                window, 'Add to front', 'Enter item:')
            if ok:
                deque_view.add_front(item)

        def remove_front_item():
            deque_view.remove_front()

        def add_rear_item():
            item, ok = QInputDialog.getText(
                window, 'Add to rear', 'Enter item:')
            if ok:
                deque_view.add_rear(item)

        def remove_rear_item():
            deque_view.remove_rear()

        add_front_button.clicked.connect(add_front_item)
        remove_front_button.clicked.connect(remove_front_item)
        add_rear_button.clicked.connect(add_rear_item)
        remove_rear_button.clicked.connect(remove_rear_item)

        layout.addWidget(deque_view)
        layout.addWidget(add_front_button)
        layout.addWidget(remove_front_button)
        layout.addWidget(add_rear_button)
        layout.addWidget(remove_rear_button)

        self.window_DAD = QWidget()
        self.window_DAD.setWindowTitle('DualArrayDeque window')
        self.window_DAD.setGeometry(500, 500, 500, 500)
        self.window_DAD.setLayout(layout)
        self.window_DAD.show()

    def open_window_rootish_array_stack(self):
        self.window_RAS = QWidget()
        self.window_RAS.setWindowTitle('RootishAraayStack window')
        self.window_RAS.setGeometry(500, 500, 500, 500)
        self.window_RAS.show()

    # funcion para centrar los botenes en el menu principal
    def center_buttons(self, buttons):
        layout = QVBoxLayout()
        layout.addStretch()
        for button in buttons:
            layout.addWidget(button)
        layout.addStretch()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
