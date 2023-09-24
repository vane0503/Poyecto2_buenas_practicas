from NodoSimple import Node
prueba=Node("Ejemplo")
print(prueba)
prueba2=Node([1,2,3,4])
print("prueba2:",prueba2)
#llamar metodo desde otra ubicacion
from ListaSimple import Lista
lista_1=Lista()
print("Nodo Inicial: ",lista_1.first)
lista_1.adicionarInicio("Universidad")
print("Nodo Inicial: ",lista_1.first)
lista_1.adicionarInicio("Costa")
print("Nodo Inicial: ",lista_1.first)
print("Siguiente Nodo Inicial:", lista_1.first.next)
print("Lista:",lista_1.verLista())
lista_1.adicionarInicio(156)
print("lista:",lista_1.verLista())
lista_1.agregarFinal(12)
