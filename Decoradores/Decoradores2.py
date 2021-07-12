from time import time
def performance(fn):
  def wrapper(*args, **kwargs):
    t1 = time()
    result = fn(*args, **kwargs)
    t2 = time()
    print(f'took {t2-t1}')
    return result
  return wrapper

@performance
def long_time():
    for i in range(10000):
        for j in range(1000):
            i*5
            i*j

long_time()