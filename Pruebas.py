from Nodos import NodoSimple
#nodo_prueba = NodoSimple("Ejemplo")
#print(nodo_prueba)
#nodo_02= NodoSimple([1,2,3,4,5])
#print("Nodo 02:",nodo_02)

from listas import ListaSimple
lista_01 = ListaSimple()
print("Nodo Inicial:", lista_01.NodoInicial)
lista_01.adicionarInicio("Universidad")
print("Nodo Inicial:", lista_01.NodoInicial)
lista_01.adicionarInicio("Costa")
print("Nodo Inicial:", lista_01.NodoInicial)
print("Siguiente Nodo Inicial:", lista_01.NodoInicial.siguiente)
print("Lista:", lista_01.verlista())
lista_01.adicionarInicio(156)
print("Lista:", lista_01.verlista())




