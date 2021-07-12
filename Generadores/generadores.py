def generador_funcion(num):
    for i in range(num):
        yield i*2

# for item in generador_funcion(1000):
#     print(item)

g = generador_funcion(1000)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
