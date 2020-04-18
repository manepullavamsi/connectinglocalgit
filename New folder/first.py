j=str(input("enter a binary frmt string"))
s=0;c=0
for i in range(len(j)-1,-1,-1):
    v=int(j[i])
    s+=v*(2**c)
    c+=1
print(s)
 
