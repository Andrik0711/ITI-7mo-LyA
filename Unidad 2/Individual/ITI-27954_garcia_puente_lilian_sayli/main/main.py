"""
Este codigo crea una ventana con un cuadro de texto y dos botones. 
El primer botón calcula los componentes fuertemente conectados del 
grafo dirigido representado por la matriz de adyacencia en el cuadro 
de texto y muestra los componentes en una nueva ventana. 
El segundo botón muestra el grafo dirigido representado 
por la matriz de adyacencia en una nueva ventana.
"""


"""
Instalar las siguientes librerias para correr el codigo:
    pip install PyQt5
    pip install networkx
    pip install matplotlib
    pip install numpy
"""


"""
Desarrollado por: 
JOSE ANDRIK MARTINEZ RODRIQUEZ
LILIAN SAYLI GARCIA PUENTE
"""




import sys
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QTextEdit
class MainWindow(QMainWindow):
    def __init__(self):
        """
        Crea una ventana con un cuadro de texto y dos botones.
        """
        super().__init__()

        # Crea una etiqueta y un cuadro de texto para la entrada de matriz.
        self.matrix_label = QLabel("Ingrese la matriz de adyacencia:")
        self.matrix_textbox = QTextEdit(self)

        # Crea un botón para activar el cálculo y la visualización de los componentes fuertemente conectados.
        self.compute_button = QPushButton(
            "Calcular componentes fuertemente conectados", self)
        self.compute_button.clicked.connect(
            self.compute_strongly_connected_components)

        # Crea un botón para mostrar el grafo dirigido a partir de la matriz de adyacencia.
        self.graph_button = QPushButton(
            "Mostrar el grafo dirigido a partir de la matriz de adyacencia", self)
        self.graph_button.clicked.connect(self.show_input_matrix_graph)

        # Propiedades de la ventana principal.
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle(
            "Proyecto Individual (Equipo) Unidad 2 ")

        # Agrega widgets a la ventana principal.
        self.matrix_label.move(50, 50)
        self.matrix_label.resize(300, 30)
        self.matrix_textbox.move(50, 80)
        self.matrix_textbox.resize(400, 300)
        self.compute_button.move(50, 400)
        self.compute_button.resize(400, 30)
        self.graph_button.move(50, 450)
        self.graph_button.resize(400, 30)

    def compute_strongly_connected_components(self):
        """
        Toma la matriz de adyacencia del cuadro de texto, 
        crea un grafo dirigido a partir de ella utilizando NetworkX, 
        calcula los componentes fuertemente conectados del grafo y 
        luego dibuja el grafo con cada componente fuertemente conectado 
        coloreado de manera diferente.
        """

        # Obtiene la matriz de adyacencia del cuadro de texto.
        adjacency_matrix_str = self.matrix_textbox.toPlainText()
        adjacency_matrix = np.array(
            [list(map(int, row.split())) for row in adjacency_matrix_str.split("\n")])

        # Crea un grafo dirigido a partir de matriz de adyacencia usando NetworkX
        graph = nx.DiGraph(adjacency_matrix)

        # Componentes fuertemente conectados
        sccs = nx.strongly_connected_components(graph)

        # Dibujar componentes fuertemente conectados
        plt.figure(figsize=(10, 10))
        pos = nx.circular_layout(graph)
        node_colors = ["red", "blue", "green", "purple", "orange", "yellow", "gray", "brown", "pink",
                       "cyan", "magenta", "olive", "teal", "gold", "navy", "maroon", "lavender"]
        color_index = 0
        for scc in sccs:
            subgraph = graph.subgraph(scc)
            nx.draw_networkx(subgraph, pos=pos,
                             node_color=node_colors[color_index])
            color_index += 1
        plt.axis("off")
        plt.show()

    def show_input_matrix_graph(self):
        """
        Toma la matriz de adyacencia del cuadro de texto, 
        crea un gráfico dirigido a partir de ella usando NetworkX,
        y luego dibuja el gráfico usando Matplotlib.
        """
        # Obtener matriz de adyacencia del cuadro de texto
        adjacency_matrix_str = self.matrix_textbox.toPlainText()
        adjacency_matrix = np.array(
            [list(map(int, row.split())) for row in adjacency_matrix_str.split("\n")])

        # Crear el grafo dirigido a partir de matriz de adyacencia usando NetworkX
        graph = nx.DiGraph(adjacency_matrix)

        # Dibuja el grafo dirigido
        plt.figure(figsize=(10, 10))
        pos = nx.circular_layout(graph)
        nx.draw_networkx(graph, pos=pos)
        plt.axis("off")
        plt.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
