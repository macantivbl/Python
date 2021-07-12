lista = ['a','b','c','b','d','m','n','n']

duplicados = list(set([value for value in lista if lista.count(value)>1 ]))

print(duplicados )


