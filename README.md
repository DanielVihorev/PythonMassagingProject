
🐍 Python Multi-User Chat Application

Secure Chat Server & Client — Cross-Network Communication

© All rights reserved to Daniel Vihorev & Ilay Zendani (Wild Life Cyber Security)

⸻

📌 Project Overview

This project is a lightweight, scalable Python-based chat system built using sockets and the select module. It enables multiple users to communicate in real-time, even if they are not on the same local network. The server handles multiple concurrent client connections, and each client must authenticate with a username and password upon connection.

Ideal for learning about:
	•	Socket programming
	•	Multi-threading
	•	Authentication flow
	•	Client-server architecture

⸻

🚀 Features
	•	🔐 Login system: Requires username and password at connection
	•	🌐 Cross-network support: Clients can connect from different networks
	•	📡 Multi-user chat: Server handles multiple concurrent clients
	•	⚙️ Non-blocking I/O with select for efficient message handling
	•	🖥️ Terminal-based interface for simplicity and transparency

⸻

📁 Project Structure

chat-app/
├── server.py     # The main server logic
├── client.py     # Client-side application
└── README.md     # Project documentation


⸻

⚙️ How It Works

Server
	•	Listens for incoming client connections.
	•	On connection, prompts the client to enter username and password.
	•	Authenticates clients and manages message broadcasting using select.

Client
	•	Connects to the server by IP and port.
	•	Sends credentials for authentication.
	•	Can send and receive messages from other users in real-time.

⸻

🛠️ Technologies Used
	•	Python 3.x
	•	socket
	•	select
	•	threading (optional for improvements)
	•	Plain terminal/console interface

⸻

🧪 How to Run

Server

python server.py

Client

python client.py

📝 Make sure to update the server IP and port in client.py before running.

⸻

🔒 Future Improvements
	•	Encryption (TLS or custom)
	•	GUI using Tkinter or PyQt
	•	Persistent user database (e.g. SQLite or MongoDB)
	•	Chat rooms / Private messaging
	•	Logging and audit trails

⸻

👥 Authors
	•	Daniel Vihorev
	•	Ilay Zendani

(Wild Life Cyber Security)

⸻

📜 License

All rights reserved to Daniel Vihorev and Ilay Zendani (Wild Life Cyber Security).
For educational or private use only. Commercial usage prohibited without written permission.

⸻