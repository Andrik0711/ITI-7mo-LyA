import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Creamos el botón
        self.button = QPushButton('Abrir ventana', self)
        self.button.clicked.connect(self.show_new_window)

        # Creamos el layout y agregamos el botón
        layout = QVBoxLayout()
        layout.addWidget(self.button)

        # Creamos el widget principal y establecemos el layout
        widget = QWidget()
        widget.setLayout(layout)

        # Establecemos el widget principal como el widget central de la ventana
        self.setCentralWidget(widget)

    def show_new_window(self):
        # Creamos una nueva instancia de la ventana secundaria
        new_window = SecondaryWindow()
        new_window.show()


class SecondaryWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Creamos una etiqueta y un botón para cerrar la ventana
        label = QLabel('Ventana secundaria')
        close_button = QPushButton('Cerrar', self)
        close_button.clicked.connect(self.close)

        # Creamos el layout y agregamos los widgets
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(close_button)

        # Establecemos el layout en la ventana
        self.setLayout(layout)
        self.setWindowTitle('Ventana secundaria')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
