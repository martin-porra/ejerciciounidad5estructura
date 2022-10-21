import numpy as np
class Nodo:
    __cantidad = None
    __siguiente = None

    def __init__(self,can):
        self.__cantidad = can
        self.__siguiente = None

    def getnombre(self):
        return self.__nombre

    def setsiguiente(self, sig):
        self.__siguiente = sig

    def getsiguiente(self):
        return self.__siguiente

    def getcantidad(self):
        return self.__cantidad


class Lista:
    __cabeza = None
    __cant = None

    def __init__(self):
        self.__cant = 0
        self.__cabeza = None


    def insertar(self,cantidad):
        nuevo = Nodo(cantidad)
        aux = self.__cabeza
        if self.__cabeza == None:
            self.__cabeza = nuevo
            self.__cabeza.setsiguiente(None)
            self.__cant+=1
        elif float(aux.getcantidad()) > float(cantidad):
            nuevo.setsiguiente(aux)
            self.__cabeza = nuevo
            self.__cant+=1
        else:
            while aux.getsiguiente() != None and float(aux.getsiguiente().getcantidad()) < float(cantidad):
                aux = aux.getsiguiente()
            nuevo.setsiguiente(aux.getsiguiente())
            aux.setsiguiente(nuevo)
            self.__cant+=1

    def recorrer(self):
        aux = self.__cabeza
        while aux != None:
            print('{0: .2f}'.format(aux.getcantidad()))
            aux = aux.getsiguiente()

    def cantidad(self):
        return  self.__cant

    def vacia(self):
        return (self.__cant == 0)

if __name__ == '__main__':
    lista = Lista()
    lista.insertar(5454)
    lista.insertar(2323)
    lista.insertar(1)
    lista.recorrer()
