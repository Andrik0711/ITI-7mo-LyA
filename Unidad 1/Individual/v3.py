import sys
import json
import networkx as nx
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QAction, QFileDialog
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor, QPolygonF
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsItem, QMenu, QAction, QGraphicsLineItem, QGraphicsEllipseItem


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.grafo = nx.DiGraph()

        self.view = QGraphicsView()
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)
        self.setCentralWidget(self.view)

        self.crear_acciones()
        self.crear_menus()

        self.setWindowTitle("Editor de grafos")

    def crear_acciones(self):
        self.accion_paste = QAction("Pegar", self)
        self.accion_paste.setShortcut("Ctrl+V")
        self.accion_paste.triggered.connect(self.pegar_grafo)

    def crear_menus(self):
        self.menu_archivo = self.menuBar().addMenu("Archivo")
        self.menu_archivo.addAction(self.accion_paste)

    def pegar_grafo(self):
        datos = json.loads(QApplication.clipboard().text())
        self.grafo.clear()
        self.scene.clear()
        for nodo in datos["nodos"]:
            self.grafo.add_node(nodo["id"], **nodo["atributos"])
            x, y = self.view.width() * \
                nodo["atributos"]["pos"][0], self.view.height() * \
                nodo["atributos"]["pos"][1]
            self.agregar_nodo(x, y)
        for arista in datos["aristas"]:
            self.grafo.add_edge(
                arista["origen"], arista["destino"], **arista["atributos"])
            self.agregar_arista(arista["origen"], arista["destino"])

    def agregar_nodo(self, x, y):
        item = NodoItem()
        item.setPos(x, y)
        self.scene.addItem(item)

    def agregar_arista(self, origen, destino):
        origen_item = self.scene.findChild(NodoItem, f"nodo_{origen}")
        destino_item = self.scene.findChild(NodoItem, f"nodo_{destino}")
        item = AristaItem(origen_item, destino_item)
        self.scene.addItem(item)

    def guardar_grafo(self):
        archivo, _ = QFileDialog.getSaveFileName(
            self, "Guardar archivo", "", "JSON (*.json)")
        if archivo:
            nodos = []
            aristas = []
            for nodo in self.grafo.nodes(data=True):
                nodo_data = {"id": nodo[0], "atributos": nodo[1]}
                nodos.append(nodo_data)
            for arista in self.grafo.edges(data=True):
                arista_data = {
                    "origen": arista[0], "destino": arista[1], "atributos": arista[2]}
                aristas.append(arista_data)
            datos = {"nodos": nodos, "aristas": aristas}
            with open(archivo, "w") as f:
                json.dump(datos, f, indent=4)

    def abrir_grafo(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
