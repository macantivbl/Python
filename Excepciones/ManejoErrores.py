while True:
    try:
        edad = int(input('Cual es tu edad?'))
        print(edad)
    except:
        print('pon un numero')
    else:
        print('Gracias')
        break

while True:
    try:
        print('pon el numero a dividir')
        numero  = int(input())
        print(10 / numero)
    except ValueError:
        print('pon un numero')
    except ZeroDivisionError:
        print('imposible hacer la divicion a cero')
    else:
        break

