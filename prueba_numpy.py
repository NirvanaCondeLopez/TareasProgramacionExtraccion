import numpy as np

l = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
n1 = np.array(l)
print(n1)
print(type(n1))

##principales atributos

print(n1.ndim)
print(n1.shape)
print(n1.size)
print(n1.dtype)

#### Acceso a los elementos
print(n1[1, 1])  # primer numero es el renglon,segundo numero es la columna

print(n1 + 2)

print(np.linalg.norm(n1))
print(n1.transpose())  # transpuesta
print(n1.mean())
print(n1[0, :].mean())

""""  
    Ecuaciones

        x+y=1
        3x+5y=2      

"""""
ecuaciones = [[1, 2], [3, 5]]
resultados = np.array([1, 2])
np_ecuaciones = np.array(ecuaciones)
print(np.linalg.solve(np_ecuaciones, resultados))