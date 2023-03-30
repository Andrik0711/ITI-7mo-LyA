import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QTabWidget
from ArrayStack import ArrayStack
from FastArrayStack import FastArrayStack
from ArrayQueue import ArrayQueue
from ArrayDeque import ArrayDeque
from DualArrayDeque import DualArrayDeque
from RootishArrayStack import RootishArrayStack


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Estructuras de datos")
        self.AS = ArrayStack()
        self.FAS = FastArrayStack()
        # Crear pestañas
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tab6 = QWidget()

        # Agregar pestañas a la ventana principal
        self.tabs.addTab(self.tab1, "ArrayStack")
        self.tabs.addTab(self.tab2, "FastArrayStack")
        self.tabs.addTab(self.tab3, "ArrayQueue")
        self.tabs.addTab(self.tab4, "ArrayDeque")
        self.tabs.addTab(self.tab5, "DualArrayDeque")
        self.tabs.addTab(self.tab6, "RootishArrayStack")

        # Agregar widgets a la pestaña ArrayStack
        self.as_label = QLabel("ArrayStack")
        self.as_textedit = QTextEdit()
        self.as_pushbutton = QPushButton("Push")
        self.as_popbutton = QPushButton("Pop")
        self.as_pushbutton.clicked.connect(self.AS.push)
        self.as_popbutton.clicked.connect(self.AS.pop)

        # Agregar widgets a la pestaña FastArrayStack
        self.fas_label = QLabel("FastArrayStack")
        self.fas_textedit = QTextEdit()
        self.fas_pushbutton = QPushButton("Push")
        self.fas_popbutton = QPushButton("Pop")
        self.fas_pushbutton.clicked.connect(self.FAS.push)
        self.fas_popbutton.clicked.connect(self.FAS.pop)

        # # Agregar widgets a la pestaña ArrayQueue
        # self.aq_label = QLabel("ArrayQueue")
        # self.aq_textedit = QTextEdit()
        # self.aq_pushbutton = QPushButton("Enqueue")
        # self.aq_popbutton = QPushButton("Dequeue")
        # self.aq_pushbutton.clicked.connect(self.enqueue_to_aq)
        # self.aq_popbutton.clicked.connect(self.dequeue_from_aq)

        # # Agregar widgets a la pestaña ArrayDeque
        # self.ad_label = QLabel("ArrayDeque")
        # self.ad_textedit = QTextEdit()
        # self.ad_pushfrontbutton = QPushButton("Push Front")
        # self.ad_pushbackbutton = QPushButton("Push Back")
        # self.ad_popfrontbutton = QPushButton("Pop Front")
        # self.ad_popbackbutton = QPushButton("Pop Back")
        # self.ad_pushfrontbutton.clicked.connect(self.pushfront_to_ad)
        # self.ad_pushbackbutton.clicked.connect(self.pushback_to_ad)
        # self.ad_popfrontbutton.clicked.connect(self.popfront_from_ad)
        # self.ad_popbackbutton.clicked.connect(self.popback_from_ad)

        # # Agregar widgets a la pestaña DualArrayDeque
        # self.dad_label = QLabel("DualArrayDeque")
        # self.dad_textedit = QTextEdit()
        # self.dad_pushfrontbutton = QPushButton("Push Front")
        # self.dad_pushbackbutton = QPushButton("Push Back")
        # self.dad_popfrontbutton = QPushButton("Pop Front")
        # self.dad_popbackbutton = QPushButton("Pop Back")
        # self.dad_pushfrontbutton.clicked.connect(self.pushfront_to_dad())
        # self.ad_pushbackbutton.clicked.connect(self.pushback_to_dad)
        # self.ad_popfrontbutton.clicked.connect(self.popfront_from_dad)
        # self.ad_popbackbutton.clicked.connect(self.popback_from_dad)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
