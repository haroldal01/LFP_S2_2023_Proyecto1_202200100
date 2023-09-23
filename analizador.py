from collections import namedtuple
from aritmeticas import *
from expresion import *
from trigonometricas import *
from imagenes.graficas import *

Token = namedtuple("Token", ["valor", "fila", "columna"])
fila = 1
columna = 1
tokens = []
errores =[]
config = {"texto":None,"fondo":None,"fuente":None,"forma":None}



class Error():
    def __init__(self,character,line,column):
        self.character = character
        self.line = line
        self.column = column

    def to_json(self):
        return {
            "descripcion:":{
            "Lexema": self.character,
            "Tipo":"error lexico",
            "fila": self.line,
            "columna": self.column
            }
        }




def stringt(entrada, i):
    token = ""
    for char in entrada:
        if char == '"':
            return [token, i]
        token += char
        i += 1
    print("no se cerró", token)



def numerot(entrada, i):
    token = ""
    decimal = False
    for char in entrada:
        if char.isdigit():
            token += char
            i += 1
        elif char == ".":
            token += char
            i += 1
            decimal = True
        else:
            break
    if decimal:
        return [float(token), i]

    return [int(token), i]


def entradat(entrada):
    global fila, columna, tokens

    i = 0
    while i < len(entrada):
        char = entrada[i]
        if char.isspace():
            if char == "\n":
                fila += 1
                columna = 1
            elif char == "\t":
                columna += 4
            i += 1
        elif char == '"':
            string, pos = stringt(entrada[i + 1:], i)
            columna += len(string) + 1
            i = pos + 2
            token = Token(string, fila, columna)
            tokens.append(token)
        elif char in ["{", "}", "[", "]", ",", ":"]:
            columna += 1
            i += 1
            token = Token(char, fila, columna)
            tokens.append(token)
        elif char.isdigit():
            number, pos = numerot(entrada[i:], i)
            columna += pos - i
            i = pos
            token = Token(number, fila, columna)
            tokens.append(token)
        else:
            print("caracter desconocido:",char,"en fila:",fila,"columna:",columna) 
            error = Error(char,fila,columna) #se inicializa la clase error
            errores.append(error)
            i += 1
            columna += 1




def obtener_instruccion():
    global tokens
    operacion = None
    value1 = None
    value2 = None
    while tokens:
        token = tokens.pop(0)
        if token.valor  == "operacion":
            tokens.pop(0)
            operacion = tokens.pop(0).valor 
        elif token.valor  == "valor1":
            
            tokens.pop(0)
            value1 = tokens.pop(0).valor 
            if value1 == "[":
                value1 = obtener_instruccion()
        elif token.valor  == "valor2":
           
            tokens.pop(0)
            value2 = tokens.pop(0).valor 
            if value2 == "[":
                value2 = obtener_instruccion()
        
        elif token.valor  in ["texto","fondo","fuente","forma"]:
            tokens.pop(0)
            config[token.valor ] = tokens.pop(0).valor 
        
        else:
            pass
        
        if operacion and value1 and value2:
            return operacionAritmetica(operacion, value1, value2,0,0)
        elif operacion and operacion in ["seno"] and value1:
            return operacionTrigonometrica(operacion, value1,0,0)
    return None

def crear_instrucciones():
    global tokens
    instrucciones = []
    while tokens:
        instruccion = obtener_instruccion()
        if instruccion:
            instrucciones.append(instruccion)
    return instrucciones



def analizar(entrada):
    entradat(entrada)
    diagrama.dot.clear()
    diagrama.aggconfiguracion(config)
    instrucciones = crear_instrucciones()
    for i in instrucciones:
        print("RESULTADO INSTRUCCION: ", i.interpretar())

    return diagrama

def reportar(entrada):
    entradat(entrada)
    diagrama.dot.clear()
    diagrama.aggconfiguracion(config)
    instrucciones = crear_instrucciones()
    for i in instrucciones:
        print("RESULTADO INSTRUCCION: ", i.interpretar())
    return diagrama     


