"""
    At least 1 letter between [a-z]
    At least 1 number between [0-9]
    At least 1 letter between [A-Z]
    At least 1 character from [$#@]
    Minimum length of transaction password: 6
    Maximum length of transaction password: 12
     [r"[a-z]", r"[A-Z]", r"[0-9]", r"[$|#|@]"]
"""
import re
def validadorPass(contra):
    password = [r"[a-zA-Z]",r"[0-9]",r"[$|@|#]"]
    for x in password:
        if not re.search(x,contra):
            print("contraseña no valida")
            return False
    if 6<=len(contra)<=12:
        return True
    else:
        print("contraseña no cumple con la longitud pedida")
        return False

contra = str(input("Ingrese la contraseña: "))

x = validadorPass(contra)
print(x)