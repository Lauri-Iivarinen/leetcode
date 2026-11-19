def climbStairs(self, n: int) -> int:
    # fibonacci
    def fib(a, n):
        if n < 0:
            return a[-1] if len(a) > 0 else 0
        if len(a) == 0:
            a = [1]
        elif len(a) == 1:
            a.append(1)
        else:
            a.append(a[-1] + a[-2])
        n = n - 1
        return fib(a, n)
        
    return fib([], n)


for i in range(1,46):
    print(i, climbStairs(None, i))

# 1 - 1
# 1

# 2 - 2
# 1 1
# 2

# 3 - 3
# 1 1 1
# 1 2
# 2 1

# 4 - 5
# 1 1 1 1
# 2 1 1
# 1 2 1
# 1 1 2
# 2 2


# 5 - 8
# 1 1 1 1 1
# 2 1 1 1
# 1 2 1 1
# 1 1 2 1
# 1 1 1 2
# 2 2 1
# 2 1 2
# 1 2 2


# 6 - 13 
# 1 1 1 1 1 1 
# 2 1 1 1 1
# 1 2 1 1 1
# 1 1 2 1 1 
# 1 1 1 2 1
# 1 1 1 1 2
# 2 2 1 1
# 2 1 2 1
# 2 1 1 2
# 1 2 2 1
# 1 2 1 2
# 1 1 2 2
# 2 2 2

