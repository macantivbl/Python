#Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.
#New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.

texto = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."

NTexto = sorted(set(texto.split()))

for x in NTexto:
    print("{0} : {1}".format(x,texto.count(x)))
"""
from pprint import pprint
p=input().split()
pprint({i:p.count(i) for i in p})
"""

"""
ver la documentacion de una funcion
"""
def pow(n,p):
    '''
    param n: This is any integer number
    param p: This is power over n
    return:  n to the power p = n^p
    '''

    return n**p

print(pow(3,4))
print(pow.__doc__)