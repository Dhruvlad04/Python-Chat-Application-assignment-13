import socket
import threading
import tkinter as tk

from layout import ChatLayout


class ChatClient:
    def __init__(self, display_callback):
        self.host = '127.0.0.1'
        self.port = 5556
        self.client_socket = None
        self.display_callback = display_callback
        self.running = False

    def connect(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client_socket.connect((self.host, self.port))
            self.running = True
            self.display_callback(f"[*] Connected to server at {self.host}:{self.port}")
            threading.Thread(target=self.receive_messages, daemon=True).start()
        except ConnectionRefusedError:
            self.display_callback("[*] Server is not running. Connection failed.")

    def receive_messages(self):
        while self.running:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if not message:
                    break
                self.display_callback(f"Server: {message}")
            except:
                break
        self.display_callback("[*] Disconnected from server.")

    def send_message(self, message):
        if self.client_socket and self.running:
            try:
                self.client_socket.send(message.encode('utf-8'))
                self.display_callback(f"You: {message}")
            except Exception as e:
                self.display_callback(f"[*] Error sending message: {e}")
        else:
            self.display_callback("[*] Not connected to a server.")

    def stop(self):
        self.running = False
        if self.client_socket:
            self.client_socket.close()


def main():
    root = tk.Tk()
    root.title("Client Side")
    root.geometry("400x500")

    backend = None
    layout = None

    def display_message(msg):
        if layout:
            root.after(0, layout.display_message, msg)

    def send_message(msg):
        if backend:
            backend.send_message(msg)

    layout = ChatLayout(root, "Client Side", send_message)
    backend = ChatClient(display_message)
    backend.connect()

    def on_closing():
        if backend:
            backend.stop()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()


if __name__ == "__main__":
    main()
