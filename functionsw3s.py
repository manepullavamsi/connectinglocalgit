def hello(k):
    k=k-1
    if k == 0:
        return k
    t=hello(k-1)
    
print(hello(5))
