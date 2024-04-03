def print1ToN_for(n):
    for i in range(1,n+1):
        print(i)
    return

def print1ToN_while(n):
    i=1
    while i <= n:
        print(i)
        i=i+1
    return

def print1ToN_rec(n):
    print1ToN(1,n)

def print1ToN(i,n):
    if i>n: return
    else:
        print(i)
        print1ToN(i+1,n)

print1ToN_for(5)
print1ToN_while(5)
print1ToN_rec(5)
