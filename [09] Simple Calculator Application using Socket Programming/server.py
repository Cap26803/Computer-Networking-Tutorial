import socket

HOST = 'localhost'  # Standard loopback interface address (localhost)
PORT = 50007        # Port to listen on (non-privileged ports are > 1023)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print(f"Server listening on {HOST}:{PORT}")

while True:
    data, address = server_socket.recvfrom(1024)  # Receive request from client
    try:
        expression = data.decode('utf-8')
        result = str(eval(expression))  # Evaluate expression
        server_socket.sendto(result.encode('utf-8'), address)  # Send result to client
    except Exception as e:
        error_message = f"Error: {e}"
        server_socket.sendto(error_message.encode('utf-8'), address)
