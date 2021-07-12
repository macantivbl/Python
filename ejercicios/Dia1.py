"""
Write a program
which will find all such numbers which are
divisible by 7 but are not a multiple of 5, between 2000 and 3200
(both included).
The numbers obtained should be printed in a
comma-separated sequence on a single line.
"""
def divisible7(num):
    if num%7 == 0:
        return True

def divisible5(num):
    if num%5 == 0:
        return True

listaAceptable = [x for x in range(2000, 3200) if divisible7(x) and not divisible5(x)]
#print(*(i for i in range(2000, 3201) if i%7 == 0 and i%5 != 0), sep=",")
print(listaAceptable)
""""
Write a program which can compute the factorial 
of a given numbers.
The results should be printed in a comma-separated 
sequence on a single line.Suppose the following 
input is supplied to the program: 8 Then, 
the output should be:40320
"""
def factorial(num):
    if num == 1:
        return num
    return (num*factorial(num-1))

while True:
    try:
        num = int(input("Pon un numero: "))
        break
    except ValueError as err:
        print(err)
org= num
print(f'el factorial de {org} es {factorial(num)}')

""""
With a given integral number n, 
write a program to generate a dictionary 
that contains (i, i x i) such that is an integral 
number between 1 and n (both included). and then the 
program should print the dictionary.Suppose the 
following input is supplied to the program: 8
"""

print('Escribe el diccionario')
n = int(input())
d = dict()
for i in range(1,n+1):
    d[i] = i * i
print(d)