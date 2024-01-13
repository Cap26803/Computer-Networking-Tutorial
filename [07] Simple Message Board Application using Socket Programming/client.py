import socket

HOST = 'localhost'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    message = input("Enter your message: ")
    client_socket.sendall(message.encode('utf-8'))

    # Receive and display server responses (optional for real-time feel)
    data = client_socket.recv(1024).decode('utf-8')
    if data:
        print(data)
