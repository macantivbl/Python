def suma_argumentos(*args):
	return sum(args)

print(suma_argumentos(1,32,43,1,2,23,1))

def highest_even(*li):
    even = list(li)
    even.sort()
    for x in even:
        if x % 2 == 0:
            return x
    return "no hay numeros pares"
