import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QComboBox
# from array_stack import ArrayStack
# from array_queue import ArrayQueue
# from array_deque import ArrayDeque
# from rootish_array_stack import RootishArrayStack
# from dual_array_deque import DualArrayDeque


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Crear instancias de las estructuras de datos
        # self.array_stack = ArrayStack()
        # self.array_queue = ArrayQueue()
        # self.array_deque = ArrayDeque()
        # self.rootish_array_stack = RootishArrayStack()
        # self.dual_array_deque = DualArrayDeque()

        # Crear los widgets de la interfaz gráfica
        self.struct_combo = QComboBox()
        self.struct_combo.addItems([
            'ArrayStack', 'ArrayQueue', 'ArrayDeque', 'RootishArrayStack', 'DualArrayDeque'
        ])
        self.size_label = QLabel('Size:')
        self.size_edit = QLineEdit()
        self.add_label = QLabel('Add element:')
        self.add_edit = QLineEdit()
        self.add_button = QPushButton('Add')
        self.remove_label = QLabel('Remove element:')
        self.remove_edit = QLineEdit()
        self.remove_button = QPushButton('Remove')
        self.table = QTableWidget()

        # Configurar la tabla
        self.table.setColumnCount(1)
        self.table.setHorizontalHeaderLabels(['Elements'])

        # Configurar los layouts
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.struct_combo)
        hbox1.addWidget(self.size_label)
        hbox1.addWidget(self.size_edit)
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.add_label)
        hbox2.addWidget(self.add_edit)
        hbox2.addWidget(self.add_button)
        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.remove_label)
        hbox3.addWidget(self.remove_edit)
        hbox3.addWidget(self.remove_button)
        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addWidget(self.table)

        # Conectar los botones a los métodos correspondientes
        self.add_button.clicked.connect(self.add_element)
        self.remove_button.clicked.connect(self.remove_element)

        # Configurar la ventana principal
        self.setLayout(vbox)
        self.setWindowTitle('Data Structures')
        self.show()

    def add_element(self):
        struct_name = self.struct_combo.currentText()
        struct_size = int(self.size_edit.text())
        struct_add = self.add_edit.text()

        # Obtener la estructura de datos seleccionada
        if struct_name == 'ArrayStack':
            struct = self.array_stack
        elif struct_name == 'ArrayQueue':
            struct = self.array_queue
        elif struct_name == 'ArrayDeque':
            struct = self.array_deque
        elif struct_name == 'RootishArrayStack':
            struct = self.rootish_array_stack
        else:
            struct = self.dual_array_deque

        # Agregar el elemento a la estructura de datos
        if struct_size == 0:
            struct.add(struct_add)
        else:
            struct.add(struct_add, struct_size)

        # Actualizar la tabla
        self.update_table()

    def remove_element(self):
        struct_name = self.struct_combo.currentText()
        struct_remove = self.remove_edit.text()

        # Obtener la estructura de datos seleccionada
        if struct_name == 'ArrayStack':
            struct = self.array_stack
        elif struct_name == 'ArrayQueue':
            struct = self.array_queue
        elif struct_name == 'ArrayDeque':
            struct = self.array_deque
        elif struct_name == 'RootishArrayStack':
            struct = self.rootish_array_stack
        else:
            struct = self.dual_array_deque

        # Remover el elemento de la estructura de datos
        struct.remove(struct_remove)

        # Actualizar la tabla
        self.update_table()

    def update_table(self):
        struct_name = self.struct_combo.currentText()

        # Obtener la estructura de datos seleccionada
        if struct_name == 'ArrayStack':
            struct = self.array_stack
        elif struct_name == 'ArrayQueue':
            struct = self.array_queue
        elif struct_name == 'ArrayDeque':
            struct = self.array_deque
        elif struct_name == 'RootishArrayStack':
            struct = self.rootish_array_stack
        else:
            struct = self.dual_array_deque

        # Actualizar la tabla
        self.table.clearContents()
        self.table.setRowCount(len(struct))
        for i, element in enumerate(struct):
            item = QTableWidgetItem(str(element))
            self.table.setItem(i, 0, item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MainWidget()
    sys.exit(app.exec_())
