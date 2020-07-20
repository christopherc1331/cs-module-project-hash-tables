# Your code here
import math
import random
import time


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v


my_dict = {}


def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """

    check_key = (x, y)

    if check_key in my_dict:
        return my_dict[check_key]

    else:
        v = math.pow(x, y)
        v = math.factorial(v)
        v //= (x + y)
        v %= 982451653
        my_dict[check_key] = v
        return v

    # Your code here


# Do not modify below this line!
start = time.time()


for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    # print(f'{i}: {x},{y}: {slowfun(x, y)}')
    slowfun(x, y)


end = time.time()
print(f"time elapsed: {start - end}")
