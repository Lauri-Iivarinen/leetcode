import math

# sure is slow...
def mySqrt(self, x: int) -> int:
    i = 1
    while (i * i <= x):
        i += 1
    return i - 1



def t(v):
    print(v, mySqrt(None, v), math.sqrt(v))
for i in range(10):
    t(i)