def fib(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        temp = a
        a = b
        b = temp + b

print(list(fib(32)))
x = fib(100)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

