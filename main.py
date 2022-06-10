from Grafo import *

a = Grafo(5)
a.arco(1,2,3)
a.arco(2,3,2)
a.arco(3,4,10)
a.arco(4,5,9)
a.arco(5,1,4)

print("ady:\n")
a.ady()
print("cost:\n")
a.cost()
a.hamilton(1)