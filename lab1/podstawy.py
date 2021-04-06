import numpy as np

a = np.zeros(10)
b = np.ones(10)*5
c= np.arange(10, 51, 1)

print("Tablica zer: ", end="")
print(a, "\n")
print("Tablica piątek: ", end="")
print(b, "\n")
print("Tablica 10-50: ", end="")
print(c, "\n")


d =  np.arange(0, 9).reshape(3,3)
print("Macierz 3x3: ")
print(d, "\n")

e = np.eye(3)
print("Macierz jednostkowa 3x3: ")
print(e, "\n")

mu, sigma = 0, 0.1
f = np.random.normal(mu, sigma, 25).reshape(5,5)
print("Macierz 5x5: ")
print(f, "\n")

g =  np.arange(0.01, 1.01, 0.01).reshape(10,10)
print("Macierz 10x10: ")
print(g, "\n")

h = np.arange(0, 1.05, 0.05)
print("Tablica 20 liniowo rozłożonych liczb: ")
print(h, "\n")

i = np.random.randint(1, 25, 25)
i = i.reshape(5, 5)
print("Macierz 5x5: ")
print(i, "\n")

print("Suma: ", end='')
print(np.sum(i))

print("Średnia: ", end='')
print(np.mean(i))

print("Standardowa dewiacja: ", end='')
print(np.std(i))

print("Suma w każdej z kolumn: ", end='')
print(i.sum(axis=0), "\n")

j = np.random.randint(100, size=(5, 5))
print("Macierz 5x5: ")
print(j, "\n")

print("Mediana: ", end='')
print(np.median(j))

print("Najmiejsza: ", end='')
print(np.min(j))

print("Największa: ", end='')
print(np.max(j), "\n")

k = np.random.randint(100, size=(4, 6))
print("Macierz 4x6: ")
print(k, "\n")
print("Macierz 6x4: ")
print(np.transpose(k), "\n")


l = np.random.randint(10, size=(5,7))
m = np.random.randint(10, size=(5, 7))
print("Macierz l 5x7: ")
print(l, "\n")
print("Macierz m 5x7: ")
print(m, "\n")
print("Suma macierzy l i m : ")
print(l.__add__(m), "\n")

n = np.random.randint(10, size=(5,9))
o = np.random.randint(10, size=(9, 6))
print("Macierz n 5x9: ")
print(n, "\n")
print("Macierz o 9x6: ")
print(o, "\n")
print("Macierz n*o pierwszym sposobem: ")
print(np.matmul(n, o), "\n")
print("Macierz n*o drugim sposobem: ")
print(n.dot(o))
