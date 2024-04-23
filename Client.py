import socket
import threading

# Function to handle receiving messages from the server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(4096).decode()
            if message:
                print(message)
        except:
            print("Connection to server lost.")
            break

# Client configuration
server_host = 'localhost'  # Change this to the server's IP address
server_port = 12345
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_host, server_port))

# Start a thread to receive messages from the server
receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()

# Main loop to send messages to the server
while True:
    message = input()
    client_socket.send(message.encode())
