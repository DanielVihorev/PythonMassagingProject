import socket
import threading
import tkinter as tk
from tkinter import simpledialog, scrolledtext, messagebox

class ChatClient:
    def __init__(self, master):
        self.master = master
        self.master.title("Tkinter Chat Client")

        # Chat display
        self.chat_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, state='disabled', width=60, height=20)
        self.chat_area.pack(padx=10, pady=10)

        # Message entry
        self.entry = tk.Entry(master, width=50)
        self.entry.pack(side=tk.LEFT, padx=10, pady=5)
        self.entry.bind("<Return>", self.send_message)

        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.LEFT, padx=5)

        self.client_socket = None
        self.receive_thread = None

        self.connect_to_server()

    def connect_to_server(self):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect(("localhost", 12346))
            self.receive_thread = threading.Thread(target=self.receive_messages)
            self.receive_thread.daemon = True
            self.receive_thread.start()

            self.handle_auth_flow()
        except Exception as e:
            messagebox.showerror("Connection Error", f"Could not connect to server: {e}")
            self.master.quit()

    def handle_auth_flow(self):
        # Read initial server prompt
        server_msg = self.client_socket.recv(4096).decode()
        self.append_message(server_msg)
        action = simpledialog.askstring("Login or Register", "Type 'l' to login or 'r' to register:")
        if not action: return
        self.client_socket.send(action.strip().lower().encode())

        # Username prompt
        server_msg = self.client_socket.recv(4096).decode()
        self.append_message(server_msg)
        username = simpledialog.askstring("Username", "Enter username:")
        if not username: return
        self.client_socket.send(username.strip().encode())

        # Password prompt
        server_msg = self.client_socket.recv(4096).decode()
        self.append_message(server_msg)
        password = simpledialog.askstring("Password", "Enter password:", show='*')
        if not password: return
        self.client_socket.send(password.strip().encode())

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(4096).decode()
                if not message:
                    break
                self.append_message(message)
            except:
                break

    def send_message(self, event=None):
        message = self.entry.get()
        if message:
            try:
                self.client_socket.send(message.encode())
                self.entry.delete(0, tk.END)
            except:
                self.append_message("Failed to send message.")

    def append_message(self, message):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, message + "\n")
        self.chat_area.yview(tk.END)
        self.chat_area.config(state='disabled')


if __name__ == "__main__":
    root = tk.Tk()
    app = ChatClient(root)
    root.mainloop()
