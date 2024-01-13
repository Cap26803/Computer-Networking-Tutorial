import socket

HOST = 'localhost'  # The server's hostname or IP address
PORT = 50007        # The port used by the server

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    expression = input("Enter expression: ")
    client_socket.sendto(expression.encode('utf-8'), (HOST, PORT))  # Send expression to server

    data, _ = client_socket.recvfrom(1024)  # Receive result from server
    result = data.decode('utf-8')
    print("Result:", result)
