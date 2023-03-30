from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import sys
import json
import math
import copy

class Node:
    def __init__(self, data,x = None, y = None):
        self.data = data
        self.next = None
        self.color = qRgb(0,0,0)
        self.bgColor = qRgb(255,255,255)
        self.textColor = qRgb(0,0,0)
        self.x = x
        self.y = y
        self.linea = None

    def getPos(self):
        return [self.x,self.y]

class LinkedList:
    def __init__(self):
        self.head = None

    def actualizarPosiciones(self):
        current = self.head
        temp = 30
        while current != None:
            current.x = temp 
            current.y = 100
            temp+=100
            current = current.next

    def add(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        
        while current.next:
            current = current.next

        current.next = new_node

    def remove(self, data):
        if not self.head:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def traverse(self):
        current = self.head
        list = []
        while current:
            list.append(current)
            current = current.next
        return list

class DrawWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(1000, 800) 
        self.data = None
        self.list = LinkedList()
        self.nodoActual = None
        self.faseNodo = 0
        self.numeroBuscado = None

    def push(self):
        number, ok = QInputDialog.getInt(None, "Enter a number", "Number:")

        if ok:
            self.list.add(number)
            self.list.actualizarPosiciones()
            self.update()

    def search(self):
        number, ok = QInputDialog.getInt(None, "Enter a number", "Number:")

        if ok:
            self.numeroBuscado = number
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.recorrer)
            self.timer.start(180)

    def recorrer(self):
        if self.nodoActual == None:
            self.nodoActual = self.list.head

        if self.faseNodo == 0:
            self.nodoActual.bgColor = qRgb(255,90,0)
            self.nodoActual.textColor = qRgb(255,255,255)
            self.nodoActual.color = qRgb(255,90,0)
            if self.numeroBuscado == self.nodoActual.data:
                self.faseNodo = 7

        elif self.faseNodo == 1:

            self.nodoActual.bgColor = qRgb(255,255,255)
            self.nodoActual.textColor = qRgb(255,90,0)

        elif self.faseNodo == 2:
            self.nodoActual.linea = 80

        elif self.faseNodo == 3:
            self.nodoActual.linea = 60
        
        elif self.faseNodo == 4:
            self.nodoActual.linea = 40 
        
        
        elif self.faseNodo == 5:
            self.nodoActual.linea = 20

        elif self.faseNodo == 6:
            self.nodoActual.linea = 0

            if self.nodoActual.next != None:
                self.nodoActual = self.nodoActual.next
                self.faseNodo = -1
            else:          
                self.timer.stop()
                self.faseNodo = -1
                self.nodoActual = None
                self.numeroBuscado = None
        
        
        elif self.faseNodo == 7:
            print('a')
            self.nodoActual.bgColor = qRgb(255,90,0)
            self.nodoActual.textColor = qRgb(255,255,255)
            self.nodoActual.color = qRgb(255,90,0)

            self.timer.stop()
            self.faseNodo = -1
            self.nodoActual = None
            self.numeroBuscado = None


        if self.faseNodo >= -1 and self.faseNodo <= 5:
            self.faseNodo+=1
        self.update()
        
            
    def pop(self):
        number, ok = QInputDialog.getInt(None, "Enter a number", "Number:")
        if ok:
            self.list.remove(number)
            self.list.actualizarPosiciones()
            self.update()

    def paintEvent(self, event): #Funcion paintevent que se llama al hacer update()
        if len(self.list.traverse()) > 0:
            painter = QPainter()
            painter.begin(self)
            data = self.list.traverse()
            painter.setPen(QPen(QColor(qRgb(0,0,0)),3, Qt.SolidLine))
            
            for edge in data:
                if edge.next != None:
                    u = {}
                    u['x'] = edge.x
                    u['y'] = edge.y
                    v = {}
                    v['x'] = edge.next.x
                    v['y'] = edge.next.y

                    line = QLineF(u['x'], u['y'], v['x'], v['y']) 
                    line.setLength(line.length() - 22)

                    if edge.linea != None:
                        painter.setPen(QPen(QColor(qRgb(0,0,0)),3, Qt.SolidLine))
                        painter.drawLine(line)
                        line2 = copy.deepcopy(line)
                        line2.setLength(line.length() - (line.length()*(edge.linea/100)))
                        painter.setPen(QPen(QColor(qRgb(255,90,0)),3, Qt.SolidLine))
                        painter.drawLine(line2)
                        painter.setPen(QPen(QColor(qRgb(0,0,0)),3, Qt.SolidLine))
                    else:
                        painter.setPen(QPen(QColor(qRgb(0,0,0)),3, Qt.SolidLine))
                        painter.drawLine(line)
                    arrow_size = 10

                    angle = math.atan2(v['y'] - u['y'], v['x'] - u['x']) 

                    p1 = QPointF(int(line.x2() - arrow_size * math.cos(angle - math.pi / 6)),int(line.y2() - arrow_size * math.sin(angle - math.pi / 6)))                
                    p2 = QPointF(int(line.x2() - arrow_size * math.cos(angle + math.pi / 6)),int(line.y2() - arrow_size * math.sin(angle + math.pi / 6)))
                    
                    painter.drawLine(QLineF(line.x2(), line.y2(), p1.x(), p1.y()))
                    painter.drawLine(QLineF(line.x2(), line.y2(), p2.x(), p2.y()))
                    
            font = QFont()
            font.setPointSize(16)
            painter.setFont(font)

            for vertexx in data:
                painter.setBrush(QBrush(QColor(vertexx.bgColor), Qt.SolidPattern))
                painter.setPen(QPen(QColor(vertexx.color),3, Qt.SolidLine))
                
                vertex = {}
                vertex['x'] = vertexx.x
                vertex['y'] = vertexx.y
                painter.drawEllipse(vertex['x'] - 25, vertex['y'] - 25, 40, 40) 

                
                painter.setPen(QPen(QColor(vertexx.textColor),3, Qt.SolidLine))

                if vertexx.data > 9:
                    painter.drawText(vertex['x']-15, vertex['y'] + 5, str(vertexx.data))
                else:
                    painter.drawText(vertex['x']-11, vertex['y'] + 5, str(vertexx.data))
                
                
                painter.setPen(QPen(QColor(qRgb(255,0,0)),3, Qt.SolidLine))
                
                if vertexx.data == data[0].data:
                    if len(data) < 2: 
                        painter.drawText(vertex['x']-28, vertex['y'] + 33, str('head'))
                        painter.drawText(vertex['x']-20, vertex['y'] + 55, str('tail'))
                    else:
                        painter.drawText(vertex['x']-28, vertex['y'] + 33, str('head'))

                elif vertexx.data == data[len(data)-1].data:
                    painter.drawText(vertex['x']-20, vertex['y'] + 33, str('tail'))
                    
            painter.end()

class MainWindow(QWidget): #Clase principal
    def __init__(self, parent=None): #Construcción de la interfaz gráfica
        QWidget.__init__(self, parent)
        #Tamaño máximo de la ventana
        self.setFixedSize(1000,800)

        self.mainLayout = QVBoxLayout()
        self.inputLayout = QHBoxLayout()#Layout para ingresar datos y botones
        self.drawWidget = DrawWidget() #Widget para mostrar los dibujos

        self.btnPush = QPushButton("Push")
        self.btnPop = QPushButton("Pop")
        self.btnSearch = QPushButton("Search")

        self.btnPush.clicked.connect(self.drawWidget.push)
        self.btnPop.clicked.connect(self.drawWidget.pop)
        self.btnSearch.clicked.connect(self.drawWidget.search)

        self.inputLayout.addWidget(self.btnPush)
        self.inputLayout.addWidget(self.btnPop)
        self.inputLayout.addWidget(self.btnSearch)
        
        self.mainLayout.addLayout(self.inputLayout)
        self.mainLayout.addWidget(self.drawWidget)
        
        self.setLayout(self.mainLayout)
        self.setWindowTitle("Linked list moves")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())
