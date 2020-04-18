'''Reverse the string according to its words
Input: programming is fun

Output: fun is programming'''
inp1=str(input("enter a string"))
l=inp1.split(" ")
print(l)
for i in range(len(l)-1,-1,-1):
    print(l[i],end=" ")
