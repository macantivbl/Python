#Define a function that can receive two integer numbers in string form and compute their sum and then print it in console.
def suma(num1,num2):
    return int(num1)+int(num2)
#sum = lambda s1,s2 : int(s1) + int(s2)
print(suma("1","2"))

#Define a function that can accept two strings as input and concatenate them and then print it in console.
texto = lambda tex1,tex2 : tex1+tex2
print(texto("3","4"))

#Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.
texto2 = lambda tex1,tex2 : print(max(tex1,tex2),key=len) if len(tex1)!=len(tex2) else print(tex1+'\n'+tex2)