import socket
import threading

HOST = 'localhost'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

clients = []

def handle_client(client_socket):
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if data:  # Check for empty messages
                print(f"Received from {client_socket.getpeername()}: {data}")
                for client in clients:
                    if client != client_socket:
                        client.sendall(data.encode('utf-8'))
        except ConnectionError:
            clients.remove(client_socket)
            client_socket.close()
            print(f"Client {client_socket.getpeername()} disconnected")
            break

while True:
    client_socket, address = server_socket.accept()
    print(f"Client {address} connected")
    clients.append(client_socket)
    threading.Thread(target=handle_client, args=(client_socket,)).start()
