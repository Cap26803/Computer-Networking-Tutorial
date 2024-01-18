<a name="br1"></a> 

***DEPARTMENT OF COMPUTER SCIENCE AND***

***ENGINEERING***

**Computer Networks - 1 (19ECSC302)**

**YEAR 2023-2024**

**REPORT ON**

**“TUTORIAL EXPERIMENTS IMPLEMENTATION”**

**SUBMITTED BY**

**NAME**

**SRN**

**Roll No**

CHINMAY PARANJAPE

02FE22BCS403

44

Faculty In-charge

**Prof. U. V. Somanatti**

SCHOOL OF COMPUTER SCIENCE & ENGINEERING

Belagavi - 590008

Computer Science Department

Computer Networks - 1 (19ECSC302)



<a name="br2"></a> 

**Experiment 1:**

**To Demonstrate network commands and tools in cmd:**

**● Ipconfig**

**○** It is the fastest way to determine IP address of the computer

**● Ping:**

○ It is used to calculate round trip time by pinging another device in the network

Computer Science Department

Computer Networks - 1 (19ECSC302)



<a name="br3"></a> 

**● traceart:**

○ It is used to trace the path between source and destination

Computer Science Department

Computer Networks - 1 (19ECSC302)



<a name="br4"></a> 

**● nslookup:**

○ It helps to verify if DNS is working correctly or not

**● netstat:**

○ It is used to list the networks and their ports which are connected currently

Computer Science Department

Computer Networks - 1 (19ECSC302)



<a name="br5"></a> 

**Experiment 2:**

**Demonstration of CISCO Packet Tracer**

**● Connection between 2 PC’s:**

**● Assigning IP Address and checking it using ipconfig:**

Computer Science Department

Computer Networks - 1 (19ECSC302)



<a name="br6"></a> 

**● Pinging the connected PC’s:**

**● Request - Response: (using packet transfer)**

Computer Science Department

Computer Networks - 1 (19ECSC302)



<a name="br7"></a> 

**Experiment 3:**

**Domain Host Control Protocol in Cisco packet tracer**

**● Network topology**

**● Enabling DHCP on the server:**

Computer Science Department

Computer Networks - 1 (19ECSC302)



<a name="br8"></a> 

**Experiment 4:**

**DNS, HTTP Implementation in CISCO Packet Tracer**

**● Creating a network and pinging devices**

**● HTTP Setup & Implementation** (using ip and username)**:**

Computer Science Department

Computer Networks - 1 (19ECSC302)



<a name="br9"></a> 

**● DNS Server Setup**

**● HTTP service using both IP Address and DNS username:**

Computer Science Department

Computer Networks - 1 (19ECSC302)



<a name="br10"></a> 

**Experiment 5:**

**Assessment on Cisco Packet Tracer using given Topology:**

(Topology 2)

**● Network setup:**

Computer Science Department

Computer Networks - 1 (19ECSC302)



<a name="br11"></a> 

**● Packet Transfer from one network to another:** (KLE Tech to Wireless Home N/w)

Computer Science Department

Computer Networks - 1 (19ECSC302)



<a name="br12"></a> 

**Experiment 7:** Socket Programming

**Simple Message Board application using socket programming:**

**server.py**

import socket

import threading

HOST = 'localhost' # Standard loopback interface address (localhost)

PORT = 65432

\# Port to listen on (non-privileged ports are > 1023)

server\_socket = socket.socket(socket.AF\_INET, socket.SOCK\_STREAM)

server\_socket.bind((HOST, PORT))

server\_socket.listen()

clients = []

def handle\_client(client\_socket):

while True:

try:

data = client\_socket.recv(1024).decode('utf-8')

if data: # Check for empty messages

print(f"Received from {client\_socket.getpeername()}: {data}")

for client in clients:

if client != client\_socket:

client.sendall(data.encode('utf-8'))

except ConnectionError:

clients.remove(client\_socket)

client\_socket.close()

print(f"Client {client\_socket.getpeername()} disconnected")

break

while True:

client\_socket, address = server\_socket.accept()

print(f"Client {address} connected")

clients.append(client\_socket)

threading.Thread(target=handle\_client, args=(client\_socket,)).start()

Computer Science Department

Computer Networks - 1 (19ECSC302)



<a name="br13"></a> 

**client.py**

import socket

HOST = 'localhost' # The server's hostname or IP address

PORT = 65432

\# The port used by the server

client\_socket = socket.socket(socket.AF\_INET, socket.SOCK\_STREAM)

client\_socket.connect((HOST, PORT))

while True:

message = input("Enter your message: ")

client\_socket.sendall(message.encode('utf-8'))

\# Receive and display server responses (optional for real-time feel)

data = client\_socket.recv(1024).decode('utf-8')

if data:

print(data)

**OUTPUT:**

(single client)

(multiple client - one server)

Computer Science Department

Computer Networks - 1 (19ECSC302)



<a name="br14"></a> 

**Experiment 8:** Socket Programming

**Simple Banking application using connection oriented socket programming:**

**server.py**

import socket

import threading

HOST = 'localhost' # Standard loopback interface address (localhost)

PORT = 65432

\# Port to listen on (non-privileged ports are > 1023)

accounts = {

'12345': {'balance': 1000.00},

'67890': {'balance': 500.00}

}

server\_socket = socket.socket(socket.AF\_INET, socket.SOCK\_STREAM)

server\_socket.bind((HOST, PORT))

server\_socket.listen()

def handle\_client(client\_socket):

while True:

try:

data = client\_socket.recv(1024).decode('utf-8')

if not data:

break

request = data.split() # Split into command and arguments

command = request[0]

account\_number = request[1]

amount = float(request[2]) if len(request) > 2 else None

if command == 'check\_balance':

balance = accounts.get(account\_number, {}).get('balance', 0.00)

response = f"Your balance is: ${balance:.2f}"

elif command == 'deposit':

accounts[account\_number]['balance'] += amount

response = f"${amount:.2f} deposited successfully. New balance:

${accounts[account\_number]['balance']:.2f}"

elif command == 'withdraw':

if accounts[account\_number]['balance'] >= amount:

accounts[account\_number]['balance'] -= amount

Computer Science Department

Computer Networks - 1 (19ECSC302)



<a name="br15"></a> 

response = f"${amount:.2f} withdrawn successfully. New balance:

${accounts[account\_number]['balance']:.2f}"

else:

response = "Insufficient funds."

else:

response = "Invalid command."

client\_socket.sendall(response.encode('utf-8'))

except ConnectionError:

break

client\_socket.close()

while True:

client\_socket, address = server\_socket.accept()

print(f"Client connected from {address}")

threading.Thread(target=handle\_client, args=(client\_socket,)).start()

**client.py**

import socket

HOST = 'localhost' # The server's hostname or IP address

PORT = 65432

\# The port used by the server

client\_socket = socket.socket(socket.AF\_INET, socket.SOCK\_STREAM)

client\_socket.connect((HOST, PORT))

while True:

command = input("Enter command (check\_balance, deposit, withdraw): ")

account\_number = input("Enter account number: ")

amount = float(input("Enter amount (for deposit or withdraw): ")) if command !=

"check\_balance" else None

request = f"{command} {account\_number} {amount}" if amount else f"{command}

{account\_number}"

client\_socket.sendall(request.encode('utf-8'))

response = client\_socket.recv(1024).decode('utf-8')

print(response)

Computer Science Department

Computer Networks - 1 (19ECSC302)



<a name="br16"></a> 

**OUTPUT:**

(initialize client & server)

(check balance for account no. 12345)

(deposit amount in the account)

(withdraw amount)

Computer Science Department

Computer Networks - 1 (19ECSC302)



<a name="br17"></a> 

**Experiment 9:** Socket Programming

**Simple Calculator application using connectionless socket programming:**

**server.py**

import socket

HOST = 'localhost' # Standard loopback interface address (localhost)

PORT = 50007

\# Port to listen on (non-privileged ports are > 1023)

server\_socket = socket.socket(socket.AF\_INET, socket.SOCK\_DGRAM)

server\_socket.bind((HOST, PORT))

print(f"Server listening on {HOST}:{PORT}")

while True:

data, address = server\_socket.recvfrom(1024) # Receive request from client

try:

expression = data.decode('utf-8')

result = str(eval(expression)) # Evaluate expression

server\_socket.sendto(result.encode('utf-8'), address) # Send result to client

except Exception as e:

error\_message = f"Error: {e}"

server\_socket.sendto(error\_message.encode('utf-8'), address)

**client.py**

import socket

HOST = 'localhost' # The server's hostname or IP address

PORT = 50007

\# The port used by the server

client\_socket = socket.socket(socket.AF\_INET, socket.SOCK\_DGRAM)

while True:

expression = input("Enter expression: ")

client\_socket.sendto(expression.encode('utf-8'), (HOST, PORT)) # Send expression to server

data, \_ = client\_socket.recvfrom(1024) # Receive result from server

result = data.decode('utf-8')

print("Result:", result)

Computer Science Department

Computer Networks - 1 (19ECSC302)



<a name="br18"></a> 

**OUTPUT:**

(server - client initialization)

(addition and subtraction operation)

(multiplication operation)

(division operation)

Computer Science Department

Computer Networks - 1 (19ECSC302)



<a name="br19"></a> 

**Experiment 11**

**Wireshark Usage to capture packets in the network:**

Wireshark is a free and open-source packet analyzer. It is used for network troubleshooting,

analysis, software and communications protocol development, and education.

**Steps to implement a simple capturing experiment**

● Open Wireshark and click on your active network (in my case **WiFi**)

● Click here (**Blue Shark Icon - Top left**) and start your network capture process.

● Go to <http://www.vbsca.ca/calender/login.asp>[ ](http://www.vbsca.ca/calender/login.asp)and enter **admin123** for both username and

password

Computer Science Department

Computer Networks - 1 (19ECSC302)



<a name="br20"></a> 

● Comeback to Wireshark app and enter **TCP** in the apply filters section

● In the same way apply **UDP** filter, it will show contains of only UDP captured packets

● Now, let us find the username and password that was captured earlier (this can be found

at the bottom left of your wireshark screen) -

Computer Science Department

Computer Networks - 1 (19ECSC302)



<a name="br21"></a> 

● The orange highlighted part is the username and password (just below) that was captured.

● Also, we can check the source details that are captured

Computer Science Department

Computer Networks - 1 (19ECSC302)

