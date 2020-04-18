l1=list(map(int, input("enter a +ve integer").split(" ")))
sub=[];i=1
for v in l1:
    k=0
    if(i<len(l1)):
        s=v+l1[i]
    if (s not in sub) and (s not in l1):
        sub.append(s)
    for v1 in l1:
        if k == i or k ==(i-1):
            continue
        else:
            for su in sub:
                s1=v1+su
                if (s1 not in sub) and (s1 not in l1):
                    sub.append(s1)
        k+=1
    i+=1
sub.sort()
print(sub)
for i in range(1,sub[len(sub)-1]):
    if (i not in sub) and (i not in l1):
        print(i)
    
