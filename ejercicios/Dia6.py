""""
ABd1234@1,a F1#,2w3E*,2We3345
"""
def passwordTotal():
    password = input("Dame la contrasña: ")
    parametro1 = False #minusculas
    parametro2 = False #mayusculas
    parametro3 = False #caracter especial
    parametro3 = False #caracter especial
    parametro4 = False #numero

    if len(password) < 6 or len(password)>12:
        print("solo se acepta contraseñas con un minimo de 6 caracteres a maximo 12")
        print(f'su contraseña tiene una longitud de {len(password)}')

    try:
        for dato in password:
            if dato.isupper():
                parametro1 = True
            elif dato.islower():
                parametro2 = True
            elif dato == "$" or dato == "#" or dato == "@":
                parametro3 = True
            elif int(dato)>=0 or int(dato)<=9:
                parametro4 = True
    except:
        print('contraseña invalida')
    print(parametro1, parametro2, parametro3,parametro4)
    if parametro1 == True and parametro2== True and parametro3 == True and parametro4 == True:
        print("contraseña aceptada")
    else:
        print("contraseña invalida intentelo de nuevo")


lst = []
while True:
    s = input().split(',')
    if not s[0]:
        break
    lst.append(tuple(s))

lst.sort(key=lambda x:(x[0],int(x[1]), int(x[2])))

print(lst)
