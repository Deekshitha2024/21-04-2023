def fib(n):
    a=0
    b=1
    print(a,b,end=" ")
    i=1
    while i<=n-2:
        c=a+b
        a=b
        b=c
        i=i+1
        print(c,end=" ")
n=int(input())
fib(n)