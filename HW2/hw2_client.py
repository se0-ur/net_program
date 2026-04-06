import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)
data = sock.recv(1024)
print(data.decode())
sock.send('Seoyoung Oh'.encode())
num = sock.recv(1024)
print(num.decode())
sock.close()