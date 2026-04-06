import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 3333))

while True:
    msg = input('Enter the calculation formula: ')
    if msg == 'q':
        break

    s.send(msg.encode())

    print('Received message: ', s.recv(1024).decode())

s.close()