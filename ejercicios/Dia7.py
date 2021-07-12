#Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
def num7():
    class Multiplo7():
        def multiplo(self, numero):
            for x in range(1,numero+1):
                numero =+ 1
                yield x*7

    numero = Multiplo7()
    generador = numero.multiplo(10)

    for x in generador:
        print(x)


#A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps
#The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer
import math
pos = [0,0]

while True:
    pasos = input()
    if not pasos:
        break
    movimiento = pasos.split(" ")
    accion = movimiento[0]
    direcion = int(movimiento[1])
    if accion == "Arriba":
        pos[0] += direcion
    if accion == "Abajo":
        pos[0] -= direcion
    if accion == "Izquierda":
        pos[1] -=  direcion
    if accion == "Derecha":
        pos[1] +=  direcion

modVect = math.sqrt(pos[0]**2 + pos[1]**2)
print(f"Me encuentro en {pos} y recorri la distancia de {modVect}")


"""
Arriba 5
Arriba 4
Arriba 3
Abajo 7
Abajo 2
Abajo 7
Izquierda -1
Izquierda 2
Derecha 4
Derecha 5


Me encuentro en [-4, 8] y recorri la distancia de 8.94427190999916
"""





