import datetime
from collections import *
import datetime
from array import array
list = [1,2,3,4,5,6,7,8,9,9,9,5,5]
oracion = 'bla bla bla pensando en python nyan'
print(Counter(oracion))
print(Counter(list))

diccionario = defaultdict(lambda: 'error en intentar acceder a un elemento no existente',{'a': 1, 'b':2})
print(diccionario['a'])
print(diccionario['z'])

print(datetime.date(1994,2,23))
print(datetime.date.today())

arr = array('d',[1,2,3])
print(arr[0])