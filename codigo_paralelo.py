import ray
import time

@ray.remote
def func(x):
    time.sleep(1)
    return x * x

futures = [func.remote(i) for i in range(4)]

print(ray.get(futures))
