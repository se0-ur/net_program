import socket

def calculate(expression):
    try:
        for op in ['+', '-', '*', '/']:
            if op in expression:
                parts = expression.split(op)
                if len(parts) != 2:
                    continue
                
                num1 = int(parts[0].strip())
                num2 = int(parts[1].strip())

                if op == '+':
                    return str(num1 + num2)
                elif op == '-':
                    return str(num1 - num2)
                elif op == '*':
                    return str(num1 * num2)
                elif op == '/':
                    if num2 == 0:
                        return "Error: Division by zero"
                    return str(round(num1 / num2, 1))
        
        return "Error: Invalid expression"
    except Exception as e:
        return f"Error: {str(e)}"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 3333))
s.listen(5)
print('waiting...')

while True:
    client, addr = s.accept()
    print('Connection from:', addr)
    
    while True:
        try:
            data = client.recv(1024)
            if not data:
                break

            received_msg = data.decode().strip()
            
            if received_msg == 'q':
                break

            print(f"Received formula: {received_msg}")

            result = calculate(received_msg)

            client.send(result.encode())
            
        except Exception as e:
            print(f"Error occurred: {e}")
            client.send(b'Try again')
            break
            
    client.close()