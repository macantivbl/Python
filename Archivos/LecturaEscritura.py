try:
    with open('prueba.txt', mode='r+') as my_file:
        texto = my_file.write('oye soy yo \n')
        print(my_file.readlines())
        print(texto)
except FileNotFoundError as err:
    print('archivo no existe')
except IOError as err:
    print("error de IO")

with open('feliz.txt', mode='w') as my_file:
    texto = my_file.write(':D \n')

