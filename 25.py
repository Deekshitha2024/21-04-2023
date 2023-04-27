n=int(input())
a=0
b=1
s=a+b
i=1
if n<=0:
    print("invalid number")
elif n==1:
    print("sum is ",0)
elif n==2:
    print("Sum is ",1)
else:
    while i<= n-2:
        c=a+b
        s=s+c
        a=b
        b=c
        i=i+1
    print("sum is",s)