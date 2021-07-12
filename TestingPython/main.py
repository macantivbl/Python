def suma(num1=0):
    try:
        if num1:
            return int(num1)+5
        else:
            return 'pon un numero'
    except ValueError as err:
        print("Solo se aceptan numeros")
        return err