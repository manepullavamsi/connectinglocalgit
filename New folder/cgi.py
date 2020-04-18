t=int(input())
for i in range(t):
    a,b,c=input().split(" ")
    a=int(a)
    b=int(b)
    c=int(c)
    co=1
    while(a>0 and b>0 and c>0):
        co+=1
        if(a>b and b>c) or (b>a and a>c) or (a==b):
            a-=1
            b-=1
        elif(b>c and c>a) or (c>b and b>a) or (b==c):
            b-=1
            c-=1
        elif(c>a and a>b) or (a>c and c>b) or (a==c):
            c-=1
            a-=1
    print(co)
