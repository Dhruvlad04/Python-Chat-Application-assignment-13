import tkinter as tk
from layout import ChatLayout
from server import ChatServer
from client import ChatClient
import sys

def main():
    root = tk.Tk()
    root.withdraw() # Hide root until mode is selected
    
    choice_window = tk.Toplevel(root)
    choice_window.title("Select Chat Mode")
    choice_window.geometry("300x120")
    choice_window.resizable(False, False)
    
    selected_mode = tk.StringVar()
    
    def set_mode(mode):
        selected_mode.set(mode)
        choice_window.destroy()
        root.deiconify() 

    tk.Label(choice_window, text="Do you want to start as Server or Client?", font=("Helvetica", 11)).pack(pady=15)
    btn_frame = tk.Frame(choice_window)
    btn_frame.pack()
    
    tk.Button(btn_frame, text="Start Server", width=12, bg="#2196F3", fg="white", font=("Helvetica", 10, "bold"), command=lambda: set_mode("Server")).pack(side=tk.LEFT, padx=10)
    tk.Button(btn_frame, text="Start Client", width=12, bg="#FF9800", fg="white", font=("Helvetica", 10, "bold"), command=lambda: set_mode("Client")).pack(side=tk.LEFT, padx=10)
    
    root.wait_window(choice_window)
    
    mode = selected_mode.get()
    if not mode:
        sys.exit()

    backend = None
    layout = None
    
    def display_message(msg):
        # Update GUI from a different thread safely
        if layout:
            root.after(0, layout.display_message, msg)
            
    def send_message(msg):
        if backend:
            backend.send_message(msg)
            
    layout = ChatLayout(root, f"Python Chat Application - {mode}", send_message)
    
    if mode == "Server":
        backend = ChatServer(display_message)
        backend.start()
    elif mode == "Client":
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
