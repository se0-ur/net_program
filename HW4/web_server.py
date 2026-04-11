import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(10)

while True:
    c, addr = s.accept()

    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')

    if req[0].startswith('GET'):

        filename = req[0].split()[1].lstrip('/')
        if filename == '': filename = 'index.html'

        if filename in ['index.html', 'iot.png', 'favicon.ico']:
            if filename == 'index.html':
                f = open(filename, 'r', encoding='utf-8')
                mimeType = 'text/html; charset =utf-8'
            elif filename == 'iot.png' : 
                f = open(filename, 'rb')
                mimeType = 'image/png'
            elif filename == 'favicon.ico':
                f = open(filename, 'rb')
                mimeType = 'image/x-icon'

            c.send(b'HTTP/1.1 200 OK\r\n')
            c.send(b'Content-Type: ' + data.encode() + b'\r\n')
            c.send(b'\r\n')

            content = f.read()
            if isinstance(content, str):
                c.send(content.encode('utf-8'))
            else:
                c.send(content)
            f.close()   

        else:
            c.send(b'HTTP/1.1 404 Not Found\r\n')
            c.send(b'\r\n')
            c.send(b'<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>')
            c.send(b'<BODY>Not Found</BODY></HTML>')

    c.close()   