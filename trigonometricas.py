from expresion import *
import math
from imagenes.graficas import *


class operacionTrigonometrica(Expresion):
    def __init__(self, tipo, valor, fila, columna):
        self.tipo = tipo
        self.valor = valor
        self.fila = fila
        self.columna = columna

    def interpretar(self):
        valor = self.valor

       
        nodo = None

        
        if isinstance(self.valor, Expresion):
            valor = self.valor.interpretar()
            nodo = diagrama.obtener_ultimo_nodo()
        else:
            valor = self.valor
            nodo = diagrama.agregar(str(valor))

        print("="*30)
        print("Operación: ", self.tipo)
        print("valor: ", valor)
       

        resultado = None


        if self.tipo == "seno":
            resultado = math.sin(valor)

        elif self.tipo =="coseno":
            resultado = math.cos(valor)

        elif self.tipo == "tangente":
            resultado = math.tan(valor)

        # GRAFICAR
        raiz = diagrama.agregar(f"{self.tipo}\\n{str(round(resultado,2))}")
        diagrama.agregar_arista(raiz, nodo)

        return round(resultado, 3)
