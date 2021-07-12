""""
Write a program that accepts a sequence of whitespace
separated words as input and prints the words after removing all
duplicate words and sorting them alphanumerically.
hello world and practice makes perfect and hello world again
"""
def palabras():
    word = sorted(list(set(input().split())))
    print(word)
    print(" ".join(word))


""""
Write a program which accepts a sequence of comma separated 
4 digit binary numbers as its input and then check whether 
they are divisible by 5 or not. The numbers that are divisible by 5 are 
to be printed in a comma separated sequence.
0100,0011,1010,1001
salida -> 1010
"""
#print(*(binary for binary in input().split(',') if int(binary,base=2)%5==0))
def binarios():
    datos = [x for x in input().split(",") if int(x, 2) % 5 == 0]
    print(datos)

""""
Write a program, which will find all 
such numbers between 1000 and 3000 (both included) such that each digit of 
the number is an even number.The numbers obtained should be printed in a 
comma-separated sequence on a single line.
"""
def es_parDigito(num):
    if (int(num[0])%2 == 0) and (int(num[1])%2 == 0) and (int(num[2])%2 == 0 and (int(num[3])%2 == 0) ):
        return True
def Respuesta():
    valores = []
    for num in range(1000, 3001):
        s = str(num)
        if es_parDigito(s):
            valores.append(s)
    print(" ".join(valores))


""""
hello world! 123
"""
print("Escribe el texto")
texto = input()
numeros, letras = 0,0
for dato in texto:
    if dato.isalpha():
        letras += 1
    elif dato.isnumeric():
        numeros += +1

print(f'Numeros {numeros}')
print(f'Letras {letras}')

word = input()
letter, digit = 0,0

