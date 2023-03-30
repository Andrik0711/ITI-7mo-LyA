import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel


class MatrixStack:
    def __init__(self):
        self.stack = [None] * 10  # rootish array with capacity for 10 elements
        self.size = 0

    def push(self, matrix):
        if self.size == len(self.stack):
            # grow the array by 10 elements if it's full
            self.stack += [None] * 10
        self.stack[self.size] = matrix
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        matrix = self.stack[self.size]
        self.stack[self.size] = None
        return matrix


class MatrixStackApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Matrix Stack")
        self.setGeometry(100, 100, 400, 300)

        self.matrix_stack = MatrixStack()

        # UI elements
        self.matrix_label = QLabel(
            "Enter a matrix in the format '1 2 3; 4 5 6; 7 8 9':")
        self.matrix_input = QLineEdit()
        self.add_button = QPushButton("Add to stack")
        self.add_button.clicked.connect(self.add_matrix)
        self.pop_button = QPushButton("Pop from stack")
        self.pop_button.clicked.connect(self.pop_matrix)
        self.stack_label = QLabel("Matrix stack:")
        self.stack_display = QLabel()

        # layout
        matrix_layout = QHBoxLayout()
        matrix_layout.addWidget(self.matrix_label)
        matrix_layout.addWidget(self.matrix_input)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.pop_button)

        stack_layout = QVBoxLayout()
        stack_layout.addWidget(self.stack_label)
        stack_layout.addWidget(self.stack_display)
        stack_layout.addLayout(matrix_layout)
        stack_layout.addLayout(button_layout)

        central_widget = QWidget()
        central_widget.setLayout(stack_layout)

        self.setCentralWidget(central_widget)

    def add_matrix(self):
        matrix_str = self.matrix_input.text()
        matrix = []
        for row_str in matrix_str.split(';'):
            row = [int(x) for x in row_str.split()]
            matrix.append(row)
        self.matrix_stack.push(matrix)
        self.update_stack_display()
        self.matrix_input.clear()

    def pop_matrix(self):
        matrix = self.matrix_stack.pop()
        if matrix is None:
            return
        self.update_stack_display()

    def update_stack_display(self):
        stack_str = ""
        for i in range(self.matrix_stack.size-1, -1, -1):
            matrix = self.matrix_stack.stack[i]
            if matrix is None:
                continue
            matrix_str = ""
            for row in matrix:
                row_str = " ".join(str(x) for x in row)
                matrix_str += row_str + "; "
            matrix_str = matrix_str[:-2]
            stack_str += matrix_str + "\n"
        self.stack_display.setText(stack_str)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MatrixStackApp()
    window.show()
    sys.exit(app.exec_())
