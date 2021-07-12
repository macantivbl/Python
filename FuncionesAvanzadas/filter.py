my_list = [0,1,2,3,4,5,6,7,8,9,56,87,94,102,157,1023547548]
def ultimo_numero(numero):
    if numero == 0:
        return 5
    return int(str(numero)[-1])

def es_par(num):
    num = ultimo_numero(num)
    if num == 2 or num == 4 or num == 6 or num == 8 or num == 0:
        return True
    return False

def only_odd(item):
    return es_par(item)

print(es_par(my_list[0]))
y = list(filter(only_odd, my_list))
print(y)
print(my_list)


