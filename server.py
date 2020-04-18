import socket
s=socket.socket()#two arguments one ipv4 or ipv6 and type of connection whether it is tcp or udp
print("socket created")
s.bind(('localhost',9999))#it takes 2 argumets one ipaddress and port number range of port no:0-65535
s.listen(3)#specfyining how many clients accept
print("waiting for connection")
while True:
    c,add=s.accept()#it gives clinent socket and client address
    name=c.recv(1024).decode()
    print("client connented",add,name)
    c.send(bytes("welcome to server","utf-8"))
    c.close()
