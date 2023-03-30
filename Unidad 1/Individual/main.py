import json
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog, QLabel

"""
Desarrollador JOSE ANDRIK MARTINEZ RODRIGUEZ
Matricula 2030152
Lenguajes y Automatas
"""

# Clase principal


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    # Crear la ventana
    def initUI(self):
        self.setWindowTitle('JSON a Representacion')
        self.setGeometry(100, 100, 600, 400)

        # Crear la interfaz
        self.text_edit = QTextEdit(self)
        self.text_edit.setAcceptRichText(False)
        self.text_edit.setPlainText("Carga tu archivo JSON.")
        self.resultado_label = QLabel(self)

        # Crear los botones
        self.cargar_btn = QPushButton('Cargar archivo', self)
        self.cargar_btn.clicked.connect(self.cargar_archivo)
        self.procesar_btn = QPushButton('Procesar', self)
        self.procesar_btn.clicked.connect(self.procesar_json)

        # Crear los layouts
        vbox = QVBoxLayout()
        vbox.addWidget(self.text_edit)
        hbox = QHBoxLayout()
        hbox.addWidget(self.cargar_btn)
        hbox.addWidget(self.procesar_btn)
        vbox.addLayout(hbox)
        vbox.addWidget(self.resultado_label)

        # Establecer el layout principal
        self.setLayout(vbox)

    # Cargar archivo json o copiar
    def cargar_archivo(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Selecciona el archivo JSON", "", "JSON Files (*.json)", options=options)
        if file_name:
            with open(file_name, 'r') as f:
                self.text_edit.setPlainText(f.read())

    # Procesa el archivo recibido
    def procesar_json(self):
        json_text = self.text_edit.toPlainText()

        # Realiza la conversion de JSON al Representacion
        try:
            data = json.loads(json_text)
            grafo = {}
            for key, value in data['el'].items():
                nodo1 = str(value['u'])
                nodo2 = str(value['v'])
                peso = str(value['w'])

                if nodo1 not in grafo:
                    grafo[nodo1] = set()

                if nodo2 not in grafo:
                    grafo[nodo2] = set()

                grafo[nodo1].add(nodo2)
                grafo[nodo2].add(nodo1)

            resultado = "Representacion de un GRAFO:\n"
            resultado += "g = {"

            for nodo, aristas in grafo.items():
                aristas_str = ", ".join([f'"{nodo2}"' for nodo2 in aristas])
                resultado += f'\n    "{nodo}" : {{ {aristas_str} }},'
            resultado += "\n}"
            self.resultado_label.setText(resultado)

        except Exception as e:
            self.resultado_label.setText(f"Error al procesar JSON: {str(e)}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
