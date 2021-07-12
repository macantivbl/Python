import math
def ejercicio1():
    valor = input("pon los numeros separados por coma")
    list = valor.split(",")
    tupla = tuple(list)
    print(list)
    print(tupla)
#print(tuple(input("Enter a series of numbers separated by a comma :").split(',')))

def ejercicio2():
    class leeImprime():
        def __init__(self):
            self.s = ""
        def get_string(self):
            self.s = input()
        def print_String(self):
            print(self.s.upper())

    objeto = leeImprime()
    objeto.get_string()
    objeto.print_String()


#Q = Square root of [(2 _ C _ D)/H]
#C is 50. H is 30.
def ejercicio3():
    dato = input('dame los numeros separados por coma:  ')
    dato = dato.split(",")
    lista = []

    for x in dato:
        i = math.sqrt((100 * int(x)) / 30)
        lista.append(round(i))

    print(lista)
""""
from math import sqrt
C, H = 50, 30
mylist = input().split(',')
print(*(round(sqrt(2*C*int(D)/H)) for D in mylist), sep=",")
"""
def arreglos():
    x,y = map(int, input("dame los dos datos: ").split(' '))
    lista = []

    for i in range(x):
        tmp = []
        for j in range(y):
            tmp.append(i*j)
        lista.append(tmp)

    print(lista)

#x,y = map(int,input().split(','))
#lst = [[i*j for j in range(y)] for i in range(x)]
#print(lst)

def acomodarPalabras():
    datos = input("dame las palabras: ").split(",")
    datos.sort()
    print(datos)

lst = []

while True:
    x = input()
    if len(x)==0:
        break
    lst.append(x.upper())

for line in lst:
    print(line)