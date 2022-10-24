import random

import numpy as np
from Lista import Nodo
class Hash:
    __tamaño= None
    __arreglo = None

    def __init__(self,tamaño):
        self.__tamaño= int(tamaño/0.7)
        self.__arreglo = np.empty(self.__tamaño,dtype=Nodo)

    def getdireccion(self,clave):
        clave = str(clave)
        lista = [str(a) for a in clave]
        n1= lista[0]+lista[1]
        n2= lista[2]+lista[3]
        direccion= ((int(n1)+int(n2))%self.__tamaño)
        return int(direccion)


    def insertar(self,clave):
        di = self.getdireccion(clave)
        nodo = Nodo(clave)
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
            if isinstance(aux,Nodo):
             c = ''
             while aux != None:
                c+=  str(aux.getclave()) +' -- '
                aux = aux.getsig()
             print(c)

    def buscar(self,clave):
        di = self.getdireccion(clave)
        band = False
        aux = self.__arreglo[di]
        while band != True and aux != None:
         if aux.getclave() == clave:
             band = True
         else:
             aux= aux.getsig()
         if band ==True:
             print('Se encontro la clave')
         else:
             print('No se encuentra la clave')
    def sinonimas(self):
        for i in range(1,1000):
            cont = 0
            aux = self.__arreglo[i]
            if isinstance(aux,Nodo):
                while aux.getsig() != None:
                    cont += 1
                    aux = aux.getsig()
                print('Longitud de lista sinonima ',cont)





if __name__ == '__main__':
    objeto = Hash(1000)
    for i in range(1000):
        x= random.randint(1000,9999)
        objeto.insertar(x)
    objeto.mostrar()
    objeto.sinonimas()