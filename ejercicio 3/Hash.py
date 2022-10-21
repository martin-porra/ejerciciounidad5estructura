import numpy as np
from Lista import Lista
class Hash:
    __tamaño= None
    __arreglo = None

    def __init__(self,tamaño):
        self.__tamaño= int(tamaño/0.7)
        self.__arreglo = np.empty(self.__tamaño,dtype=Lista)

    def getdireccion(self,clave):
        clave = str(clave)
        lista = [str(a) for a in clave]
        n1= lista[0]+lista[1]+lista[2]+lista[3]
        n2= lista[4]+lista[5]
        direccion= ((int(n1)+int(n2))%self.__tamaño)
        return int(direccion)


    def insertar(self,clave):
        di = self.getdireccion(clave)
        nodo = Lista(clave)
        if self.__arreglo[di] == None:
            self.__arreglo[di] = nodo
        elif self.__arreglo[di].getclave() == clave:
            print('ELemento ya existente')
        else:
            aux = self.__arreglo[di].getsig()
        while aux != None:
            aux = self.__arreglo[di].getsig()
            aux = nodo
    def mostrar(self):
        for i in range(self.__tamaño):
            aux = self.__arreglo[i]
            while aux != None:
                print(aux.getclave())



if __name__ == '__main__':
    objeto = Hash(1000)
    objeto.insertar(999999)
    objeto.insertar(129000)
    objeto.mostrar()