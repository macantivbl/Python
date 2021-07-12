def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('/***************/')
        func(*args, **kwargs)
        print('/***************/')
    return wrap_func

@my_decorator
def hola(saludo, emoji = ':D'):
    print(saludo,emoji)

hola('hola')

