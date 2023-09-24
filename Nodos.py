#Clase Nodo Simple
class NodoSimple:
    def __init__(self, info):
        self.info = info 
        self.siguiente = None

    def __str__(self): #"imprimir"
        return str(self.info)
    

