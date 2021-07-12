def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(f'pon un numero {err}')
        return 'Error'
def div(num1, num2):
    try:
        return  num1/num2
    except (TypeError, ZeroDivisionError) as err:
        print(err)
        return 'Error'

print(div(5,0))
print(sum(12, 'fdas'))

