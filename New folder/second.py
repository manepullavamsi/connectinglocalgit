s=input("enter a array")
a=[]
a=s.split(" ")
x,y=input("enter a indexs").split(" ")

x=int(x)
y=int(y)
print(x,y)
n=[]
for i in range(x-1,y):
    n.append(a[i])
n.reverse()
print(n)
c=0
for i in range(x-1,y):
    a[i]=n[c]
    c+=1
print(a)
a1=[]
for i in a:
    a1.append(int(i))
print(a1)
