import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from collections import deque

"""
DESARROLLADORES:
1-  JOSE ANDRIK MARTINEZ RODRIGUEZ  2030152
2-  CESAR ALDHAIR FLORES GAMEZ      2030070
3-  LORENA MARISOL ROMERO HERNANDEZ 2030112
4-  FRANCISCO GAEL SUSTAITA REYNA   2030048
"""

"""
Clase con las funcionalidades del metodo ArrayStack en ella se establece el evento de dibujo con propiedades de un painter que permita
dibujar los elementos, las funciones principales es apilar y desapilar elementos generados en una posicion con coordenadas x,y y generando 
un espacio entre ellas para la asignación de nuevos nodos que sean agregados en el array
"""
class ArrayStack(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Array Stack')
        self.stack = []

    """Evento para dibujar el contenido, aquí se asigna el color, y la posicón donde se encontrara cada uno de los elementos del array,
    asi mismo se da un tamaño especifico para el contenido ingresado"""
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

    # Funcion para apilar n cantidad de elementos
    def push(self, item):
        self.stack.append(item)
        self.update()

    # Funcion para desapilar elementos teniendo un top
    def pop(self):
        if len(self.stack) > 0:
            self.stack.pop()
            self.update()

""""
Clase para el desarrollo de los diferentes tipos de metodos a utilizar en el metodo Fast Array Stack, 
teniendo como principales funcionalidades el poder apilar y desapilar elementos ingresados por el usuario.
Este cuenta con un proceso más eficiente que el array stack, por ello sus procesos se optimizan.
Así mismo cuenta con un paint event para poder realizar la representación grafica de los elementos en la ventana
simulando el proceso de ingreso y retiro de los elementos 
"""
class FastArrayStack(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Fast Array Stack')
        self.stack = []
        self.top = -1
    
    """Evento para dibujar el contenido, aquí se asigna el color, y la posicón donde se encontrara cada uno de los elementos,
    asi mismo se da un tamaño especifico para el contenido ingresado"""
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

    # Funcion para apilar n cantidad de elementos
    def push(self, item):
        self.top += 1
        if self.top < len(self.stack):
            self.stack[self.top] = item
        else:
            self.stack.append(item)
        self.update()

    # Funcion para desapilar elementos teniendo un top
    def pop(self):
        if len(self.stack) > 0:
            self.stack.pop()
            self.top -= 1
            self.update()

"""
Clase del tipo de array Deque, en esta clase se presenta el paint event para la realización de visualización de los nodos
para dar una retroalimentación grafica del contenido, así mismo se establecen las 4 posibles funcionalidades que tiene dicho algoritmo
para apliar y deapilar al inicio y al final para cada uno de los dos casos anteriores realizando de manera concreta el contenido del metodo"""
class ArrayDeque(QWidget):
    def __init__(self):
        super().__init__()
        self.array = [None] * 2
        self.front = -1
        self.rear = -1

    #  Evento para dibujar el contenido de manera grafica, dando las posiciónes, tamaño y color a cada uno de los elementos del array
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

    # Funcion para apilar el contenido al inicio del array
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

    # Funcion para apilar al final del array
    def push_back(self, item):
        if self.rear == len(self.array) - 1:
            self.array += [None] * len(self.array)
        self.rear += 1
        self.array[self.rear] = item
        if self.front == -1:
            self.front = 0
        self.update()

    #Funcion para deapilar al inicio del array
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

    # Funcion para desapilar al final del arrya
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

"""
Creamos la clase ArrayQueue la cual tiene el funcionamiento de realizar
la estructura de datos ArrayQueue, aregando y quitando elementos.
"""
class ArrayQueue(QWidget):
    def __init__(self):
        super().__init__()
        self.array = [None] * 2
        self.front = -1
        self.rear = -1

    """
    El paintEvent es un método que se llama automáticamente cada vez 
    que la interfaz gráfica de usuario se actualiza, y se utiliza para 
    dibujar la cola en la pantalla. 
    """

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

    """
    Funcion la cual agrega un nuevo elemento, en dado caso que este vacio
    lo inserta en el vacio.
    """
    def enqueue(self, item):
        if self.rear == len(self.array) - 1:
            self.array += [None] * len(self.array)
        self.rear += 1
        self.array[self.rear] = item
        if self.front == -1:
            self.front = 0
        self.update()


    """
    elimina el primer elemento de la cola. 
    Si la cola está vacía, se devuelve None.
    """
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

"""
Se crea la clase DualArrayDeque la cual tiene el funcionamiento de realizar
la estructura de datos DualArrayDeque, aregando y quitando elementos 
tanto en la parte frontal como final.
"""
class DualArrayDeque(QWidget):
    def __init__(self):
        super().__init__()
        self.front = deque()
        self.rear = deque()

    """
    El paintEvent es un método que se llama automáticamente cada vez 
    que la interfaz gráfica de usuario se actualiza, y se utiliza para 
    dibujar la cola en la pantalla. 
    """
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

    """
    Agrega el elemento en la parte frontal
    """
    def add_front(self, item):
        self.front.appendleft(item)
        self.update()

    """
    Elimina el elemento de la parte frontal
    """
    def remove_front(self):
        if self.front:
            item = self.front.popleft()
            self.update()
            return item

    """
    Agrega el elemento en la parte final
    """
    def add_rear(self, item):
        self.rear.append(item)
        self.update()

    """
    ELiminar el elemento de la parte final
    """
    def remove_rear(self):
        if self.rear:
            item = self.rear.pop()
            self.update()
            return item

"""
Se crea la clase RootishArrayStack la cual tiene el funcionamiento de realizar
la estructura de datos RootishArrayStack, aregando y quitando elementos de la listas.
"""
class RootishArrayStack(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Rootish Array Stack')
        self.stack = []
        self.blocks = []

    """
    El paintEvent es un método que se llama automáticamente cada vez 
    que la interfaz gráfica de usuario se actualiza, y se utiliza para 
    dibujar la cola en la pantalla. 
    """
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(QColor(qRgb(231, 95, 95)), 2, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.white, Qt.SolidPattern))
        width = 50
        height = 30
        x = 50
        y = 50

        for block in self.blocks:
            for i, item in enumerate(block):
                rect = QRect(x, y, width, height)
                painter.drawRect(rect)
                painter.drawText(rect, Qt.AlignCenter, str(item))
                x += width + 10
            y += height + 10
            x = 50

        painter.end()

     # Funcion para apilar n cantidad de elementos dentro de una lista de listas
    def push(self, item):
        if len(self.blocks) == 0 or len(self.blocks[-1]) == int((len(self.blocks) + 1) ** 0.5):
            self.blocks.append([item])
        else:
            self.blocks[-1].append(item)
        self.stack.append(item)
        self.update()

    # Funcion para desapilar elementos teniendo un top quitando elementos de las listas de listas
    def pop(self):
        if len(self.stack) > 0:
            item = self.stack.pop()
            if len(self.blocks[-1]) == 0:
                self.blocks.pop()
            self.blocks[-1].pop()
            self.update()

"""
Creamos la clase principal para generar el menu de opciones
"""
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100,100,290,100)
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

        #centramos los botones en el menu principla
        self.center_buttons([self.buttonAS, self.buttonFAS, self.buttonAD, self.buttonAQ, self.buttonDAD, self.buttonRAS])
    
    #generamos las ventanas de los botones
    def open_window_array_stack(self):

        """
        Se crea la ventana emergente cuando da clic en la opcion del menu main
        cada ventana nueva cuenta con caracteristicas especificas de cada 
        estructura de datos
        """
        layout = QVBoxLayout()
        stack_view = ArrayStack()
        push_button = QPushButton('Push')
        pop_button = QPushButton('Pop')

        """
        Se genera la ventana emergente para agregar elementos
        """
        def push_item():
            item, ok = QInputDialog.getText(window, 'Push', 'Enter item:')
            if ok:
                stack_view.push(item)

        def pop_item():
            stack_view.pop()

        """
        Conectamos los botones con la funcion correspondiente
        """
        push_button.clicked.connect(push_item)
        pop_button.clicked.connect(pop_item)

        """
        Agregamos los widgets correspondientes
        """
        layout.addWidget(stack_view)
        layout.addWidget(push_button)
        layout.addWidget(pop_button)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(push_button)
        hbox1.addWidget(pop_button)

        vbox1 = QVBoxLayout()
        vbox1.addLayout(hbox1)

        """
        Generamos y mostramos la ventana
        """
        self.window_AS = QWidget()
        self.window_AS.setWindowTitle('ArrayStack window')
        self.window_AS.setGeometry(500, 500, 900, 900)
        self.window_AS.setLayout(layout)
        self.window_AS.show()

    def open_window_fast_array_stack(self):
        """
        Se crea la ventana emergente cuando da clic en la opcion del menu main
        cada ventana nueva cuenta con caracteristicas especificas de cada 
        estructura de datos
        """

        layout = QVBoxLayout()
        stack_view = FastArrayStack()
        push_button = QPushButton('Push')
        pop_button = QPushButton('Pop')

        """
        Se genera la ventana emergente para agregar elementos
        """
        def push_item():
            item, ok = QInputDialog.getText(window, 'Push', 'Enter item:')
            if ok:
                stack_view.push(item)

        def pop_item():
            stack_view.pop()

        """
        Conectamos los botones con la funcion correspondiente
        """
        push_button.clicked.connect(push_item)
        pop_button.clicked.connect(pop_item)

        """
        Agregamos los widgets correspondientes
        """
        layout.addWidget(stack_view)
        layout.addWidget(push_button)
        layout.addWidget(pop_button)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(push_button)
        hbox1.addWidget(pop_button)

        vbox1 = QVBoxLayout()
        vbox1.addLayout(hbox1)

        
        """
        Generamos y mostramos la ventana
        """
        self.window_FAS = QWidget()
        self.window_FAS.setWindowTitle('FastArrayStack window')
        self.window_FAS.setGeometry(500, 500, 900, 900)
        self.window_FAS.setLayout(layout)
        self.window_FAS.show()

    def open_window_array_deque(self):
        """
        Se crea la ventana emergente cuando da clic en la opcion del menu main
        cada ventana nueva cuenta con caracteristicas especificas de cada 
        estructura de datos
        """

        layout = QVBoxLayout()
        stack_view = ArrayDeque()
        push_button_1 = QPushButton('Push Front')
        pop_button_1 = QPushButton('Pop Front')
        push_button_2 = QPushButton('Push Back')
        pop_button_2 = QPushButton('Pop Back')

        """
        Se genera la ventana emergente para agregar y quitar elementos
        """

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

        """
        Conectamos los botones con la funcion correspondiente
        """
        push_button_1.clicked.connect(push_item)
        pop_button_1.clicked.connect(pop_item)
        push_button_2.clicked.connect(push_item_2)
        pop_button_2.clicked.connect(pop_item_2)

        """
        Agregamos los widgets correspondientes
        """
        layout.addWidget(stack_view)
        layout.addWidget(push_button_1)
        layout.addWidget(pop_button_1)
        layout.addWidget(push_button_2)
        layout.addWidget(pop_button_2)

        """
        Generamos y mostramos la ventana
        """
        self.window_AD = QWidget()
        self.window_AD.setWindowTitle('ArrayDeque window')
        self.window_AD.setGeometry(500, 500, 900, 900)
        self.window_AD.setLayout(layout)
        self.window_AD.show()
    
    def open_window_array_queue(self):
        """
        Se crea la ventana emergente cuando da clic en la opcion del menu main
        cada ventana nueva cuenta con caracteristicas especificas de cada 
        estructura de datos
        """

        layout = QVBoxLayout()
        queue_view = ArrayQueue()
        enqueue_button = QPushButton('Enqueue')
        dequeue_button = QPushButton('Dequeue')

        """
        Se genera la ventana emergente para agregar elementos
        """
        def enqueue_item():
            item, ok = QInputDialog.getText(window, 'push', 'Enter item:')
            if ok:
                queue_view.enqueue(item)

        def dequeue_item():
            queue_view.dequeue()

        """
        Conectamos los botones con la funcion correspondiente
        """
        enqueue_button.clicked.connect(enqueue_item)
        dequeue_button.clicked.connect(dequeue_item)

        """
        Agregamos los widgets correspondientes
        """
        layout.addWidget(queue_view)
        layout.addWidget(enqueue_button)
        layout.addWidget(dequeue_button)

        """
        Generamos y mostramos la ventana
        """
        self.window_AQ = QWidget()
        self.window_AQ.setWindowTitle('ArrayQueue window')
        self.window_AQ.setGeometry(500, 500, 900, 900)
        self.window_AQ.setLayout(layout)
        self.window_AQ.show()
    
    def open_window_dual_array_deque(self):
        """
        Se crea la ventana emergente cuando da clic en la opcion del menu main
        cada ventana nueva cuenta con caracteristicas especificas de cada 
        estructura de datos
        """

        layout = QVBoxLayout()
        deque_view = DualArrayDeque()
        add_front_button = QPushButton('Add to front')
        remove_front_button = QPushButton('Remove from front')
        add_rear_button = QPushButton('Add to rear')
        remove_rear_button = QPushButton('Remove from rear')

        """
        Se genera la ventana emergente para agregar elementos enfrente
        """
        def add_front_item():
            item, ok = QInputDialog.getText(window, 'Add to front', 'Enter item:')
            if ok:
                deque_view.add_front(item)

        def remove_front_item():
            deque_view.remove_front()

        """
        Se genera la ventana emergente para agregar elementos al final
        """

        def add_rear_item():
            item, ok = QInputDialog.getText(window, 'Add to rear', 'Enter item:')
            if ok:
                deque_view.add_rear(item)

        def remove_rear_item():
            deque_view.remove_rear()

        """
        Conectamos los botones con la funcion correspondiente
        """
        add_front_button.clicked.connect(add_front_item)
        remove_front_button.clicked.connect(remove_front_item)
        add_rear_button.clicked.connect(add_rear_item)
        remove_rear_button.clicked.connect(remove_rear_item)

        """
        Agregamos los widgets correspondientes
        """
        layout.addWidget(deque_view)
        layout.addWidget(add_front_button)
        layout.addWidget(remove_front_button)
        layout.addWidget(add_rear_button)
        layout.addWidget(remove_rear_button)

        """
        Generamos y mostramos la ventana
        """
        self.window_DAD = QWidget()
        self.window_DAD.setWindowTitle('DualArrayDeque window')
        self.window_DAD.setGeometry(500, 500, 900, 900)
        self.window_DAD.setLayout(layout)
        self.window_DAD.show()

    def open_window_rootish_array_stack(self):
        """
        Se crea la ventana emergente cuando da clic en la opcion del menu main
        cada ventana nueva cuenta con caracteristicas especificas de cada 
        estructura de datos
        """

        layout = QVBoxLayout()
        stack_view = RootishArrayStack()
        push_button = QPushButton('Push')
        pop_button = QPushButton('Pop')

        """
        Se genera la ventana emergente para agregar elementos enfrente
        """

        def push_item():
            item, ok = QInputDialog.getText(window, 'Push', 'Enter item:')
            if ok:
                stack_view.push(item)

        def pop_item():
            stack_view.pop()

        """
        Conectamos los botones con la funcion correspondiente
        """
        push_button.clicked.connect(push_item)
        pop_button.clicked.connect(pop_item)


        """
        Agregamos los widgets correspondientes
        """
        layout.addWidget(stack_view)
        layout.addWidget(push_button)
        layout.addWidget(pop_button)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(push_button)
        hbox1.addWidget(pop_button)

        vbox1 = QVBoxLayout()
        vbox1.addLayout(hbox1)

        """
        Generamos y mostramos la ventana
        """
        self.window_RAS = QWidget()
        self.window_RAS.setWindowTitle('RootishArrayStack window')
        self.window_RAS.setGeometry(500, 500, 900, 900)
        self.window_RAS.setLayout(layout)
        self.window_RAS.show()

    #funcion para centrar los botenes en el menu principal
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
