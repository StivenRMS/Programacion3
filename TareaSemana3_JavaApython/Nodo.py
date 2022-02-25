class Nodo:
    def __init__(self, dato, derecho=None, izquierdo=None):
        self.izquierdo = izquierdo
        self.derecho = derecho
        self.dato = dato


    def Valor_nodo(self):
      return self.dato

    def GetSubarbolIzdo(self):
        return self.izquierdo

    def GetSubarbolDcho(self):
        return self.derecho

    def nuevoValor(self,d):
        self.dato = d

    def setRamaIzdo(self,n):
        self.izquierdo = n

    def setRamaDcho(self,n):
        self.derecho = n        