import socket
import threading
import tkinter as tk
from tkinter import font

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                chat_log.config(state=tk.NORMAL)
                chat_log.insert(tk.END, "Server: " + message + "\n", 'server')
                chat_log.config(state=tk.DISABLED)
            else:
                break
        except:
            break

def send_message():
    message = entry.get()
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "Client: " + message + "\n", 'client')
    chat_log.config(state=tk.DISABLED)
    entry.delete(0, tk.END)
    client_socket.send(message.encode('utf-8'))


host = 'IP' #change to the server's IP. 
port = 1234
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))


root = tk.Tk()
root.title("Client Chat Simulator")

bg_color = "#2e2e2e"
fg_color = "#00ff00"
font_name = "Helvetica"
header_font = (font_name, 20, 'bold')
text_font = (font_name, 12)

header = tk.Label(root, text="Client Chat Simulator", bg=fg_color, fg="white", font=header_font)
header.pack(fill=tk.X)

chat_log = tk.Text(root, state=tk.DISABLED, width=50, height=20, bg=bg_color, fg="white", font=text_font)
chat_log.tag_configure('server', foreground="white")
chat_log.tag_configure('client', foreground=fg_color)
chat_log.pack(padx=10, pady=10)

entry = tk.Entry(root, width=40, bg="white", fg="black", font=text_font)
entry.pack(side=tk.LEFT, padx=(10, 0), pady=(0, 10))

send_button = tk.Button(root, text="Send", command=send_message, bg=fg_color, fg="white", font=text_font)
send_button.pack(side=tk.RIGHT, padx=(0, 10), pady=(0, 10))

root.configure(bg=bg_color)

receive_thread = threading.Thread(target=receive_messages)
receive_thread.daemon = True
receive_thread.start()

root.mainloop()
