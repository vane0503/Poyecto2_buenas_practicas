from Nodos import NodoSimple
#Clase Lista Simple
class ListaSimple:
    def __init__(self):
        self.NodoInicial = None

        #Adicion al Inicio
    def adicionarInicio(self, info_nuevo):
            #Creacion nuevo nodo
        nodoNuevo = NodoSimple(info_nuevo)
            #Evaluar si la lista esta vacia
        if self.NodoInicial == None:
            self.NodoInicial = nodoNuevo
        else:
            nodoNuevo.siguiente = self.NodoInicial
            self.NodoInicial = nodoNuevo
        #Recorrido
    def verlista(self):
        recorrido ="" # "o str()"
        nodoActual = self.NodoInicial
        while nodoActual != None:
            recorrido += str(nodoActual) + " "
            nodoActual = nodoActual.siguiente
        return recorrido
