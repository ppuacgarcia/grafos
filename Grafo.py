import numpy as np
from numpy import zeros


class Grafo:
    
    def __init__(self,v):
        self.v=v
        self.matC=np.zeros([v,v],float)
        self.matAd=np.zeros([v,v],int)
        
    def arco(self,nodo_i,nodo_f,costo):
        self.matC[nodo_f-1,nodo_i-1]=costo
        self.matAd[nodo_f-1,nodo_i-1]=1

    def ady(self):
        print(self.matAd)

    def cost(self):
        print(self.matC)
    def hamilton(self, inicio):
        disttotal = 0
        dist = 0
        nextnode = inicio-1
        actualnode = inicio-1
        fin = 0
        cadena = ""
        while fin < self.v:
            for i in range (self.v):
                if(self.matC[actualnode, i] != 0):
                    if(dist == 0):
                        dist = self.matC[actualnode, i]
                        nextnode = i
                    else:
                        if(self.matC[actualnode, i]<dist):
                            dist = self.matC[actualnode, i]
                            nextnode = i
            cadena = cadena + "pasa por grafo: " + str(actualnode + 1)  + " costo: " + str(dist)
            disttotal = dist + disttotal
            actualnode = nextnode
            fin = fin + 1
            
        print(disttotal)
        print(cadena)



            
            
a=Grafo(5)

