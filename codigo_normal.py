import time

def func(x):
    time.sleep(1)
    return x * x

vals = [func(i) for i in range(4)]
print(vals)

