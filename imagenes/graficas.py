import graphviz
import time


class Diagrama:
    def __init__(self):
        timestr = time.strftime("%Y%m%d-%H%M%S")
        self.dot = graphviz.Digraph(comment=f"Graph {timestr}")
        self.counter = 0

    def aggconfiguracion(self, confg):
        self.dot.attr(
            "node",
            style="filled",
            fillcolor=confg["fondo"],
            fontcolor=confg["fuente"],
            shape=confg["forma"],
        )

    def agregar(self, valor):
        nombre = f"nodo{self.counter}"
        self.dot.node(nombre, valor)
        self.counter += 1
        return nombre

    def agregar_arista(self, nodo1: str, nodo2: str):
        self.dot.edge(nodo1, nodo2)

    def generarGrafica(self):
        self.dot.render("Graficas/diagrama", view=True)
        self.dot.save("Graficas/diagrama.dot")

    def obtener_ultimo_nodo(self):
        return f"nodo{self.counter - 1}"


diagrama = Diagrama()