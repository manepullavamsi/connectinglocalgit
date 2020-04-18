test_case=int(input("enter no: test cases"))
for t in range(test_case):
    no_h,co_h=input("enter no: houses and amount have").split(" ")
    no_h,co_h=int(no_h),int(co_h)
    l=[]
    for i in range(no_h):
        l.append(int(input("enter cost")))
    l.sort()
    i=0;tc=0
    while(co_h>0 and i<len(l)):
        if(l[i]<=co_h):
            tc+=1
            co_h-=l[i]
        i+=1
    print("case#",t,tc)
        
        
