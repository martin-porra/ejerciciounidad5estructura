import numpy as np
class Nodo:
    __cantidad = None
    __siguiente = None

    def __init__(self,can):
        self.__cantidad = can
        self.__siguiente = None

    def setsig(self, sig):
        self.__siguiente = sig

    def getsig(self):
        return self.__siguiente

    def getclave(self):
        return self.__cantidad

