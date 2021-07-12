#Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
#Hello world!
def es_may_min():
    texto = input("Dame el texto: ")
    i,j = 0,0
    for dato in texto:
        if dato.isupper():
            i += 1
        elif dato.islower():
            j += 1
    print(f'Mayusculas {i} \nMinusculas {j}')
    """"
    word = input()
    upper = sum(1 for i in word if i.isupper())           # sum function cumulatively sum up 1's if the condition is True
    lower = sum(1 for i in word if i.islower())

    print("UPPER CASE {0}\nLOWER CASE {1}".format(upper,lower))
    """

#Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
def numeros():
    dato = input("Dame el numero: ")

    print(int(dato) + int(dato*2)+ int(dato*3) + int(dato*4))

    a = input()
    print(sum(int(i*a) for i in range(1,5)))


