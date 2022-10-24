import numpy as np
import random
class Tabla:
    __arreglo = None
    __tamaño = None
    __random = None
    __contador=0
    def __init__(self,tamaño=1000):
        self.__contador=0
        self.__tamaño = int(tamaño/0.7)
        self.__arreglo = np.empty(self.__tamaño,dtype=int)
        for i in range(self.__tamaño):
            self.__arreglo[i]=0


    def GetDireccion(self, clave):
        direccion = clave % self.__tamaño
        return int(direccion)

    def insertar(self,clave):
        di = self.GetDireccion(clave)

        if self.__arreglo[di] == 0:
            self.__arreglo[di] = clave
        else:
            band = False
            i = di
            j = (di+1)%self.__tamaño
            while band == False and i!=j and (self.__arreglo[j] != clave):
                if self.__arreglo[j] == 0:
                    band = True
                    self.__arreglo[j] = clave
                else:
                    j = (j+1)%self.__tamaño
    def buscar(self,clave):
        di = self.GetDireccion(clave)
        pos=None
        if self.__arreglo[di] == 0:
         print('No existe la clave')
        elif self.__arreglo[di] == clave:
         pos = di
        else:
          band = False
          i= di
          j = di+1
          while i != j and not band:
            self.__contador += 1
            if self.__arreglo[j] == clave:
             band = True
             pos = j
            else:
                j +=1
        return pos


    def mostrar(self):
        for i in range(self.__tamaño):
            if self.__arreglo[i] != 0:
                print(self.__arreglo[i])
    def rand(self):
        print(self.__random)

    def lista(self):
        lista = []
        for i in range(800):
            lista.append(self.__arreglo[i])
        for i in range(800):
            self.buscar(lista[i])
        print(self.__contador)


if __name__ == '__main__':
    tabla = Tabla(1000)
    for i in range(1000):
        x = random.randint(10700,37000)
        tabla.insertar(x)
    tabla.mostrar()
    print('cantidad de busquedas')
    tabla.lista()