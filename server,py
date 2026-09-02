import socket
import threading
import tkinter as tk
from layout import ChatLayout

class ChatServer:
    def __init__(self, display_callback):
        self.host = '127.0.0.1'
        self.port = 5556
        self.server_socket = None
        self.client_socket = None
        self.display_callback = display_callback
        self.running = False

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)
        self.running = True

        self.display_callback(f"[*] Server listening on {self.host}:{self.port}...")

        threading.Thread(target=self.accept_client, daemon=True).start()

    def accept_client(self):
        try:
            self.client_socket, address = self.server_socket.accept()
            self.display_callback(f"[*] Connected to client at {address[0]}:{address[1]}")
            self.receive_messages()
        except:
            pass

    def receive_messages(self):
        while self.running:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if not message:
                    break
                self.display_callback(f"Client: {message}")
            except:
                break
        self.display_callback("[*] Client disconnected.")
        self.client_socket = None

    def send_message(self, message):
        if self.client_socket:
            try:
                self.client_socket.send(message.encode('utf-8'))
                self.display_callback(f"You: {message}")
            except Exception as e:
                self.display_callback(f"[*] Error sending message: {e}")
        else:
            self.display_callback("[*] No client connected.")

    def stop(self):
        self.running = False
        if self.client_socket:
            self.client_socket.close()
        if self.server_socket:
            self.server_socket.close()

def main():
    root = tk.Tk()
    root.title("Server Side")
    root.geometry("400x500")

    backend = None
    layout = None

    def display_message(msg):
        if layout:
            root.after(0, layout.display_message, msg)

    def send_message(msg):
        if backend:
            backend.send_message(msg)

    layout = ChatLayout(root, "Server Side", send_message)
    backend = ChatServer(display_message)
    backend.start()

    def on_closing():
        if backend:
            backend.stop()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()


if __name__ == "__main__":
    main()

