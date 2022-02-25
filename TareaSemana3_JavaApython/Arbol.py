from Nodo import *

class Arbol:
    def __init__(self, raiz = None):
        self.raiz = raiz

    def Insertar(self, dato,padre = None):
        if padre == None:
            if self.raiz == None:
                self.raiz = Nodo(dato)
            else:
                self.Insertar(dato,self.raiz)
        else:
            if dato>padre.Valor_nodo():
                if padre.GetSubarbolDcho()== None:
                    padre.setRamaDcho(Nodo(dato))
                else:
                    if padre.GetSubarbolIzdo()== None:
                       padre.setRamaIzdo(Nodo(dato))
                    else:
                        self.Insertar(dato, padre.GetSubarbolIzdo())



        