from expresion import *
from imagenes.graficas import *
import math


class operacionAritmetica(Expresion):
    def __init__(self, tipo, v1, v2, linea, columna):
        self.tipo = tipo
        self.v1 = v1
        self.v2 = v2
        self.linea = linea
        self.columna = columna

    def interpretar(self):
        global diagrama

        v1 = self.v1
        v2 = self.v2

     
        nodo1 = None
        nodo2 = None

      
        if isinstance(self.v1, Expresion):
            v1 = self.v1.interpretar()
            nodo1 = diagrama.obtener_ultimo_nodo()
            print("RESULTADO: ", v1)
        else:
            v1 = self.v1
            nodo1 = diagrama.agregar(str(v1))
        if isinstance(self.v2, Expresion):
            v2 = self.v2.interpretar()
            nodo2 = diagrama.obtener_ultimo_nodo()
            print("RESULTADO: ", v2)
        else:
            v2 = self.v2
            nodo2 = diagrama.agregar(str(v2))

        print("OPERCION: ", self.tipo)
        print("NODOS HIJOS: ", nodo1, nodo2)

        print("=" * 30)
        print("tipo: ", self.tipo)
        print("v1: ", v1)
        print("v2: ", v2)
        print("="*30)

        
        resultado = None
        if self.tipo == "suma":
            resultado = v1 + v2

        elif self.tipo == "resta":
            resultado = v1 - v2

        elif self.tipo == "multiplicacion":
            resultado = v1 * v2

        elif self.tipo == "potencia":
            resultado = math.pow(v1, v2)

        elif self.tipo == "raiz":
            resultado = math.pow(v1, 1 / v2)

        elif self.tipo == "division":
            resultado = v1/v2

        elif self.tipo == "mod": 
            resultado = v1%v2
        
        elif self.tipo == "inverso":
            resultado = 1/v1

     
        if diagrama == None:
            print("diagrama es None")

        raiz = diagrama.agregar(f"{self.tipo}\\n{str(round(resultado))}")
        diagrama.agregar_arista(raiz, nodo1)
        if self.v2 != None:
            diagrama.agregar_arista(raiz, nodo2)

        return round(resultado,2)

    def __str__(self) -> str:
        return (
            super().__str__()
            + " tipo: "
            + self.tipo
            + " v1: "
            + str(self.v1)
            + " v2: "
            + str(self.v2)
        )