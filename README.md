# Python Chat Application

A simple two-way socket-based chat application built in Python using a server and client.

## Features
- Server listens for incoming client connections
- Client connects to the server
- Messages can be sent from client to server
- Messages can be sent from server to client
- Both sides display sent and received messages
- Separate files for server-side and client-side logic
- Tkinter-based GUI interface for each side

## Project Structure
- `server.py` - server-side application
- `client.py` - client-side application
- `layout.py` - shared chat interface design
- `main.py` - optional app launcher for selecting server or client mode

## Requirements
Python 3.x

## How to Run
### 1. Start the server
```bash
cd "d:\PYTHON.01\PythonChatApplication-Dhruv"
python server.py
```

### 2. Start the client
Open a second terminal and run:
```bash
cd "d:\PYTHON.01\PythonChatApplication-Dhruv"
python client.py
```

## How It Works
- The server opens a socket on `127.0.0.1:5556`
- The client connects to the server using the same host and port
- Each side sends and receives messages over the socket connection
- Message exchange is displayed in the chat window

## Example Output
```text
[*] Server listening on 127.0.0.1:5556...
[*] Connected to client at 127.0.0.1:xxxxx
Client: hello
You: hi
Server: hi
```

## Notes
- Run server and client in separate terminals for real-time communication.
- If the port is already in use, close the existing process or change the port number.

## Assignment Goal
This project demonstrates socket programming, client-server communication, message exchange, and GUI-based chat interaction in Python.
