import numpy as np
class Bucket:
    __contador = None
    __arreglo = None
    def __init__(self,tamaño=20):
        self.__arreglo = np.empty(tamaño,dtype=int)
        self.__contador = 0

    def insertar(self,clave):
        if not clave in self.__arreglo:
            self.__arreglo[self.__contador] = clave
            self.__contador+=1
    def mostrar(self):
        if self.__contador != 0:
            for i in range(0,self.__contador,1):
                print(self.__arreglo[i])
        else:
            print('Vacio')
    def lleno(self):
        band= False
        if self.__contador == len(self.__arreglo):
            band = True
        return band
    def __str__(self):
        x = ''
        for i in range(self.__contador):
            x += str(self.__arreglo[i]) + '--'
        return x
    def tercera(self):
        band = False
        tamaño = int(len(self.__arreglo)/3)
        if tamaño >= self.__contador:
            band= True
        return  band
    def buscar(self,clave):
        band = False
        for i in range(self.__contador):
            if self.__arreglo[i] == clave:
                band = True
        return band