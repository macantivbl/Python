my_list = [1,2,3]

def multiply_by2(item):
    return  item*2
x = map(multiply_by2, [1,2,3])
print(list(x))

#funcion lambda
print(list(map(lambda item: item*2, my_list)))