import socket

HOST = 'localhost'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    command = input("Enter command (check_balance, deposit, withdraw): ")
    account_number = input("Enter account number: ")
    amount = float(input("Enter amount (for deposit or withdraw): ")) if command != "check_balance" else None
    request = f"{command} {account_number} {amount}" if amount else f"{command} {account_number}"
    client_socket.sendall(request.encode('utf-8'))

    response = client_socket.recv(1024).decode('utf-8')
    print(response)
