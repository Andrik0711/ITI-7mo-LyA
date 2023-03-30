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


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ArrayStack Example")
        self.setGeometry(100, 100, 500, 400)

        # Create widgets
        self.label = QLabel("Agrega un caracter a la cola:")
        self.input_box = QLineEdit()
        self.add_button = QPushButton("Add")
        self.pop_button = QPushButton("Pop")
        self.stack_display = QPlainTextEdit()

        # Create layout
        hbox = QHBoxLayout()
        hbox.addWidget(self.label)
        hbox.addWidget(self.input_box)
        hbox.addWidget(self.add_button)
        hbox.addWidget(self.pop_button)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(self.stack_display)

        # Set main widget
        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)

        # Connect buttons to functions
        self.add_button.clicked.connect(self.add_item)
        self.pop_button.clicked.connect(self.pop_item)

        # Create ArrayStack object
        self.stack = ArrayStack()

    def add_item(self):
        item = self.input_box.text()
        self.stack.push(item)
        self.stack_display.setPlainText(str(self.stack.items))
        self.input_box.setText("")

    def pop_item(self):
        self.stack.pop()
        self.stack_display.setPlainText(str(self.stack.items))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
