from audioop import minmax
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
    def  hamilton(self,start):
        nv=self.v
        actual=start-1
        crrc=0
        cad=""
        minx=0
        miny=0
        for i in range(nv):
            crrc=0
            for j in range(nv):
                if(self.matC[j,actual]!=0):
                    if(crrc==0):
                        crrc=self.matC[j,actual]
                        minx=j
                        miny=actual
                    elif(crrc>self.matC[j,actual]):
                        crrc=self.matC[j,actual]
                if(j>=4):
                    cad+="["+str(miny+1)+","+str(minx+1)+"],"
           
            if(actual==nv-1):
                actual=0
            else:
                actual=actual+1
        print(cad)            


       



            
            
a=Grafo(5)

