import os

""""
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers. >Suppose the following input is supplied to the program:
entrada -> 1,2,3,4,5,6,7,8,9
salida -> 1,9,25,49,81
"""
def listaImparCuadrado():
    listaImpar = [str(int(x)**2)for x in input().split(",") if int(x)%2 != 0]
    print(",".join(listaImpar))

def menu():
    print("El banco de su preferencia elija la opcion que desea: ")
    print("1 -> Deposito")
    print("2 -> Retiro")
    print("3 -> consultar saldo")
    print("4 -> salir")
    print("")
    opcion = input()
    return opcion


def errorDato(opcion):
    while True:
        try:
            if int(opcion) >= 5 or int(opcion) <= 0:
                print("seleccione una opcion correcta")
                opcion = menu()
            elif int(opcion) <= 4:
                print("aqui")
                return int(opcion)
        except (ValueError):
            print("Solo se aceptan numeros")
            opcion = menu()



dinero = 100
while True:
    opcion = errorDato(menu())
    if(opcion == 1):
        try:
            deposito = int(input("diga la cantidad a depositar \n"))
            dinero = dinero + deposito
        except(ValueError):
            print("Solo se aceptan numeros")

    elif(opcion == 2):
        try:
            retiro = int(input("diga la cantidad a retirar \n"))
            if retiro > dinero:
                print("Saldo insuficiente")
        except(ValueError):
            print("Solo se aceptan numeros")
        else:
            dinero = dinero - retiro
    elif(opcion == 3):
        print(dinero)
    elif(opcion == 4):
        break

print("Gracias por usar el banco de mierda")