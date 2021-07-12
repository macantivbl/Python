x = 0
while True:
    try:
        numero = int(input('pon un numero'))
        print(10/numero)
    except (ValueError, ZeroDivisionError):
        print('Error en el dato dado')
    else:
        print('Gracias')
        break
    finally:
        x += 1
        if x == 5:
            print('Demasiados errores saliendo del programa')
            break