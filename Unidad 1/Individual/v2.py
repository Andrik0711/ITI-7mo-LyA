import sys
import json
import networkx as nx
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QAction, QFileDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Editor de Grafos")
        self.setGeometry(100, 100, 800, 600)

        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene)
        self.setCentralWidget(self.view)

        self.menu = self.menuBar().addMenu("Archivo")

        self.guardar_action = QAction("Guardar", self)
        self.guardar_action.triggered.connect(self.guardar_grafo)
        self.menu.addAction(self.guardar_action)

        self.abrir_action = QAction("Abrir", self)
        self.abrir_action.triggered.connect(self.abrir_grafo)
        self.menu.addAction(self.abrir_action)

        self.grafo = nx.Graph()

    def agregar_nodo(self, x, y):
        id_nodo = str(len(self.grafo.nodes()) + 1)
        self.grafo.add_node(id_nodo)
        self.scene.addEllipse(x-25, y-25, 50, 50)
        self.scene.addText(id_nodo).setPos(x-7, y-20)

    def agregar_arista(self, nodo1, nodo2):
        if nodo1 != nodo2 and not self.grafo.has_edge(nodo1, nodo2):
            self.grafo.add_edge(nodo1, nodo2)
            x1, y1 = self.scene.items()[int(
                nodo1)-1].pos().x(), self.scene.items()[int(nodo1)-1].pos().y()
            x2, y2 = self.scene.items()[int(
                nodo2)-1].pos().x(), self.scene.items()[int(nodo2)-1].pos().y()
            self.scene.addLine(x1+25, y1+25, x2+25, y2+25)

    def guardar_grafo(self):
        archivo, _ = QFileDialog.getSaveFileName(
            self, "Guardar archivo", "", "JSON (*.json)")
        if archivo:
            datos = {"nodos": [], "aristas": []}
            for nodo in self.grafo.nodes(data=True):
                datos["nodos"].append({"id": nodo[0], "atributos": nodo[1]})
            for arista in self.grafo.edges(data=True):
                datos["aristas"].append(
                    {"origen": arista[0], "destino": arista[1], "atributos": arista[2]})
            with open(archivo, "w") as f:
                json.dump(datos, f, indent=2)

    def abrir_grafo(self):
        datos = json.loads(self.clipboard.text())
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
