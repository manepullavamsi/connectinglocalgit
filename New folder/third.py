'''Problem 2: Given a string, say sentence=” this is crazy and fun” and a list, say name=[“is”, “fun”].  Now you need to capitalize on the first letter of every word in the given string which is not present in the list.

Output: “This is Crazy And fun”'''
inp1=input("enter a string")
inp2=[]
inp2=input("enter a exceptional words").split(" ")
print(inp1,inp2)
l=list(inp1.split(" "))
print(l)
s=""
for i in l:
    if i in inp2:
        s+=" "+i
    else:
        i=i.capitalize()
        s=s+" "+i
print(s)
