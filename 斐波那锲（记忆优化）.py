def fibn(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        if fib[n - 1] == 0:
            fib[n - 1] = fibn(n - 1) + fibn(n - 2)
            return fib[n - 1]
        else:
            return fib[n - 1]


fib = [1, 1]
a = int(input())
if a > 2:
    for i in range(a - 2):
        fib.append(0)
fibn(a)
for i in range(a):
    print(fib[i], end=' ')
