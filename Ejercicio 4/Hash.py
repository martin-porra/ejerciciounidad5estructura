from operator import mod
import numpy as np
import random
from Bucket import Bucket
class Hash:
    __arreglo = None
    __tamaño = None
    __overflow = None
    __total = None
    __overflowactual= None
    def __init__(self,tamaño=1000):
        self.__tamaño = int(tamaño / 20)
        self.__overflow = int(self.__tamaño * 0.3)
        band = False
        while band != True:
            self.__tamaño += 1
            band = self.es_primo(self.__tamaño)
        self.__total = self.__tamaño + self.__overflow
        self.__arreglo = np.empty(self.__total,dtype=Bucket)
        self.__overflowactual = self.__tamaño
        for i in range(self.__total):
            buck = Bucket()
            self.__arreglo[i] = buck

    def getdireccion(self,clave):
        clave = int(str(clave)[-2:])
        if clave >= self.__tamaño:
            clave = clave % self.__tamaño
        return clave

    def es_primo(self, num):
        band = True
        for n in range(2, int(num)):
            if int(num) % n == 0:
                band = False
        return band

    def insertar(self,clave):
        modulo = self.getdireccion(clave)
        if not self.__arreglo[modulo].lleno():
            self.__arreglo[modulo].insertar(clave)
        else:
            if self.__arreglo[self.__overflowactual].lleno():
                self.__overflowactual+=1
            if self.__overflowactual == self.__total-1:
                print('Arreglo lleno')
            else:
                self.__arreglo[self.__overflowactual].insertar(clave)


    def mostrar(self):
        for i in range(self.__total-1):
            print(i)
            print(self.__arreglo[i])

    def buscar(self,clave):
        band = False
        dir = self.getdireccion(clave)
        if self.__arreglo[dir].buscar(clave):
            print('se encuentra la clave')
            band= True
        else:
            for i in range(self.__tamaño,self.__total-1):
                if self.__arreglo[i].buscar(clave):
                    print('se encuentra la clave')
                    band= True
        if band == False:
            print('No se encuentra la clave ')
    def cantidad(self):
        lleno =0
        semivacio=0
        for i in range(self.__total-1):
           if self.__arreglo[i].lleno():
               lleno+=1
           if self.__arreglo[i].tercera():
               semivacio+=1
        print('La cantidad de buckets llenos es: ', lleno)
        print('La cantidad de Buckets semi vacios es: ', semivacio)

if __name__ == '__main__':
    obj = Hash()
    for i in range(0,1000):
        x = random.randint(1000,9999)
        obj.insertar(x)
    obj.mostrar()
    x = int(input())
    obj.buscar(x)
    obj.cantidad()

