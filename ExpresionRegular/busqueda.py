import re

patron = re.compile(r"([a-zA-Z]).(n)")
cadena = 'Este es un ejemplo es vicente'

a = patron.search(cadena)
b = patron.findall(cadena)

d = patron.match(cadena)
print(a)
print(b)
print(d)

print(a.group())
print(a.group(1))
print(a.group(2))


#https://regex101.com/

