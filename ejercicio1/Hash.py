import numpy as np
import random
class Tabla:
    __arreglo = None
    __tamaño = None
    __random = None
    def __init__(self,tamaño=5):
        self.__tamaño = tamaño+int(tamaño*0.7)
        self.__arreglo = np.empty(self.__tamaño,dtype=int)
        for i in range(self.__tamaño):
            self.__arreglo[i]=0
        self.__random = random.randint(1,self.__tamaño-1)


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
            j = (di+self.__random)%self.__tamaño
            while band == False and i!=j and (self.__arreglo[j] != clave):
                if self.__arreglo[j] == 0:
                    band = True
                    self.__arreglo[j] = clave
                else:
                    j = (j+self.__random)%self.__tamaño
    def buscar(self,clave):
        cont=1
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
            cont += 1
            if self.__arreglo[j] == clave:
             band = True
             pos = j
            else:
                j +=1
        print('La longitud de la secuencia de busqueda fue: ', cont )
        return pos


    def mostrar(self):
        for i in range(self.__tamaño):
            if self.__arreglo[i] != 0:
                print(self.__arreglo[i])
    def rand(self):
        print(self.__random)


if __name__ == '__main__':
    tabla = Tabla(1000)
    tabla.insertar(12200)
    for i in range(1000):
        x = random.randint(1700,1000000)
        tabla.insertar(x)

    tabla.insertar(19000)
    tabla.mostrar()
    print('Ingrese numero para buscar ')
    num = int(input())
    tabla.buscar(num)