def lcm1(a,b):
    p=1
    if a>=b:
        for i in range(1,b+1):
                if a%i==0 and b%i ==0:
                    l.append(i)
                    print(i)
                    a=a//i
                    b=b//i
                    
                else:
                    continue
    else:
        for i in range(1,a+1):
                if a%i==0 and b%i ==0:
                    l.append(i)
                    print(i)
                    a=a//i
                    b=b//i
                else:
                    continue
    for j in l:
        p=p*j
    print(p)
l=[]
a,b=map(int,input().split())
lcm1(a,b)


