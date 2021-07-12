from functools import reduce
my_list = [1,2,3]

def multiply_by2(item):
    return  item*2

def acumulador(acc,item):
    print(item, acc)
    return acc + item

print(reduce(acumulador, my_list, 0))