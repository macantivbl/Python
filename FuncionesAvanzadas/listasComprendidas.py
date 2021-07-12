my_list = []

for char in 'hello':
    my_list.append(char)

print(my_list)

mi_lista = [palabra for palabra in 'hello']

print(mi_lista)

mi_lista_numeros = [numero for numero in range(0, 100)]
mi_lista_numeros_pares = [numero for numero in range(0, 100) if numero % 2 == 0]
mi_lista_numeros2 = [numero*2 for numero in range(0, 100)]

print(mi_lista_numeros)
print(mi_lista_numeros_pares)
print(mi_lista_numeros2)

#diccionario
simple_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 5
}
my_dic = {key: value**2 for key,value in simple_dict.items()}
my_dic2 = {key: value**2 for key,value in simple_dict.items() if value%2 ==0}
print(my_dic)
print(my_dic2)