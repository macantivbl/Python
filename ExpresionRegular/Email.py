import re
patron = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
email = input("Escribe tu Email: ")

aceptar = patron.search(email)
print(aceptar)

patron2 = re.compile(r"[a-zA-Z0-9#$@}]{6,}")
contra = input("Escribe tu contraseña: ")

aceptar2 = patron2.fullmatch(contra)
print(aceptar2)
