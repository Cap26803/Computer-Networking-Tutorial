import socket
import threading

HOST = 'localhost'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

accounts = {
    '12345': {'balance': 1000.00},
    '67890': {'balance': 500.00}
}

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

def handle_client(client_socket):
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            request = data.split()  # Split into command and arguments
            command = request[0]
            account_number = request[1]
            amount = float(request[2]) if len(request) > 2 else None

            if command == 'check_balance':
                balance = accounts.get(account_number, {}).get('balance', 0.00)
                response = f"Your balance is: ${balance:.2f}"
            elif command == 'deposit':
                accounts[account_number]['balance'] += amount
                response = f"${amount:.2f} deposited successfully. New balance: ${accounts[account_number]['balance']:.2f}"
            elif command == 'withdraw':
                if accounts[account_number]['balance'] >= amount:
                    accounts[account_number]['balance'] -= amount
                    response = f"${amount:.2f} withdrawn successfully. New balance: ${accounts[account_number]['balance']:.2f}"
                else:
                    response = "Insufficient funds."
            else:
                response = "Invalid command."

            client_socket.sendall(response.encode('utf-8'))
        except ConnectionError:
            break

    client_socket.close()

while True:
    client_socket, address = server_socket.accept()
    print(f"Client connected from {address}")
    threading.Thread(target=handle_client, args=(client_socket,)).start()
