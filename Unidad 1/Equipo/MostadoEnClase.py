import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QPlainTextEdit


class ArrayStack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[-1]

    def __len__(self):
        return len(self.items)


class FastArrayStack:
    def __init__(self):
        self.items = [None] * 8
        self.size = 0

    def push(self, item):
        if self.size == len(self.items):
            self.resize(2 * len(self.items))
        self.items[self.size] = item
        self.size += 1

    def pop(self):
        self.size -= 1
        item = self.items[self.size]
        self.items[self.size] = None
        if self.size == len(self.items) // 4 and len(self.items) > 8:
            self.resize(len(self.items) // 2)
        return item

    def top(self):
        return self.items[self.size - 1]

    def __len__(self):
        return self.size

    def resize(self, new_size):
        new_array = [None] * new_size
        for i in range(self.size):
            new_array[i] = self.items[i]
        self.items = new_array


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ArrayStack")
        self.setGeometry(100, 100, 500, 400)

        # Create widgets
        self.label1 = QLabel("Agrega un valor en ArrayStack:")
        self.input_box1 = QLineEdit()
        self.add_button1 = QPushButton("Add")
        self.pop_button1 = QPushButton("Pop")
        self.stack_display1 = QPlainTextEdit()

        self.label2 = QLabel("Agrega un valor en FastArrayStack:")
        self.input_box2 = QLineEdit()
        self.add_button2 = QPushButton("Add")
        self.pop_button2 = QPushButton("Pop")
        self.stack_display2 = QPlainTextEdit()

        # Create layouts
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.label1)
        hbox1.addWidget(self.input_box1)
        hbox1.addWidget(self.add_button1)
        hbox1.addWidget(self.pop_button1)

        vbox1 = QVBoxLayout()
        vbox1.addLayout(hbox1)
        vbox1.addWidget(self.stack_display1)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.label2)
        hbox2.addWidget(self.input_box2)
        hbox2.addWidget(self.add_button2)
        hbox2.addWidget(self.pop_button2)

        vbox2 = QVBoxLayout()
        vbox2.addLayout(hbox2)
        vbox2.addWidget(self.stack_display2)

        main_vbox = QVBoxLayout()
        main_vbox.addLayout(vbox1)
        main_vbox.addLayout(vbox2)

        # Set main widget
        widget = QWidget()
        widget.setLayout(main_vbox)
        self.setCentralWidget(widget)

        # Connect buttons to functions
        self.add_button1.clicked.connect(self.add_item1)
        self.pop_button1.clicked.connect(self.pop_item1)
        self.add_button2.clicked.connect(self.add_item2)
        self.pop_button2.clicked.connect(self.pop_item2)

        # Create ArrayStack and FastArrayStack objects
        self.stack1 = ArrayStack()
        self.stack2 = FastArrayStack()

        # Update display
        self.update_display()

    def add_item1(self):
        item = self.input_box1.text()
        self.stack1.push(item)
        self.input_box1.clear()
        self.update_display()

    def pop_item1(self):
        self.stack1.pop()
        self.update_display()

    def add_item2(self):
        item = self.input_box2.text()
        self.stack2.push(item)
        self.input_box2.clear()
        self.update_display()

    def pop_item2(self):
        self.stack2.pop()
        self.update_display()

    def update_display(self):
        # Update ArrayStack display
        self.stack_display1.clear()
        for item in self.stack1.items:
            self.stack_display1.appendPlainText(str(item))

        # Update FastArrayStack display
        self.stack_display2.clear()
        for i in range(len(self.stack2)):
            item = self.stack2.items[i]
            self.stack_display2.appendPlainText(str(item))

        # Clear input boxes
        self.input_box1.clear()
        self.input_box2.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
