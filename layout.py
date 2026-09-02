import tkinter as tk
from tkinter import scrolledtext

class ChatLayout:
    def __init__(self, root, title, send_callback):
        self.root = root
        self.root.title(title)
        self.root.geometry("400x500")
        
        self.chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', font=("Helvetica", 11))
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        bottom_frame = tk.Frame(root)
        bottom_frame.pack(padx=10, pady=(0, 10), fill=tk.X, side=tk.BOTTOM)
        
        self.msg_entry = tk.Entry(bottom_frame, font=("Helvetica", 12))
        self.msg_entry.pack(fill=tk.X, side=tk.LEFT, expand=True, padx=(0, 5))
        self.msg_entry.bind("<Return>", lambda event: self.on_send(send_callback))
        
        self.send_btn = tk.Button(bottom_frame, text="Send", font=("Helvetica", 11, "bold"), bg="#4CAF50", fg="white", command=lambda: self.on_send(send_callback))
        self.send_btn.pack(side=tk.RIGHT)

    def on_send(self, callback):
        msg = self.msg_entry.get().strip()
        if msg:
            self.msg_entry.delete(0, tk.END)
            callback(msg)

    def display_message(self, message):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, message + "\n")
        self.chat_area.yview(tk.END)
        self.chat_area.config(state='disabled')
