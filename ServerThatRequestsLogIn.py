import socket
import select

# Function to broadcast messages to all connected clients
def broadcast_message(server_socket, message):
    for client_socket in connected_clients:
        if client_socket != server_socket:
            try:
                client_socket.send(message)
            except:
                # If sending fails, close the client socket
                client_socket.close()
                del connected_clients[client_socket]
                del client_usernames[client_socket]
                continue

# Server configuration
server_host = 'localhost'  # You can change this to your server's public IP
server_port = 12345
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_host, server_port))
server_socket.listen(5)

# List to keep track of connected clients and their usernames
connected_clients = {}
client_usernames = {}

print("Chat server started on {}:{}".format(server_host, server_port))

# Dictionary to store username-password pairs (for demonstration purposes only)
user_credentials = {
    "user1": "password1",
    "user2": "password2"
}

# Main loop to handle incoming connections and messages
while True:
    # Use select to multiplex input/output events
    read_sockets, _, _ = select.select(connected_clients.keys(), [], [])

    for sock in read_sockets:
        if sock == server_socket:  # New connection
            client_socket, client_address = server_socket.accept()
            print("New connection from {}:{}".format(client_address[0], client_address[1]))
            client_socket.send("Enter your username: ".encode())
            username = client_socket.recv(1024).decode().strip()
            if username in user_credentials:
                client_socket.send("Enter your password: ".encode())
                password = client_socket.recv(1024).decode().strip()
                if password == user_credentials[username]:
                    connected_clients[client_socket] = client_address
                    client_usernames[client_socket] = username
                    client_socket.send("Authentication successful. You have joined the chat.\n".encode())
                    broadcast_message(server_socket, "{} has joined the chat.\n".format(username).encode())
                else:
                    client_socket.send("Incorrect password. Connection closed.\n".encode())
                    client_socket.close()
            else:
                client_socket.send("Username not found. Connection closed.\n".encode())
                client_socket.close()
        else:  # Incoming message from a client
            try:
                message = sock.recv(4096)
                if message:
                    broadcast_message(server_socket, "{}: {}".format(client_usernames[sock], message.decode()).encode())
            except:
                broadcast_message(server_socket, "{} has left the chat.\n".format(client_usernames[sock]).encode())
                sock.close()
                del connected_clients[sock]
                del client_usernames[sock]
                continue
