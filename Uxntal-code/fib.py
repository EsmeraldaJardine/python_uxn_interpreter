
def fib(n):
    if n<=1:
        return 1
    else:
        nm1 = fib(n-1)
        nm2 = fib(n-2)
        return nm1+nm2

for n in range(11):
    print(fib(n))

