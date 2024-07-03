import socket
import threading
import tkinter as tk
from tkinter import font

clients = []

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                chat_log.config(state=tk.NORMAL)
                chat_log.insert(tk.END, "Client: " + message + "\n", 'client')
                chat_log.config(state=tk.DISABLED)
                broadcast_message(message, client_socket)
            else:
                break
        except:
            break
    clients.remove(client_socket)
    client_socket.close()

def broadcast_message(message, source_socket):
    for client in clients:
        if client != source_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                client.close()
                clients.remove(client)

def start_server():
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"[*] Listening on {host}:{port}")
    
    while True:
        client, addr = server_socket.accept()
        clients.append(client)
        print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

def send_message():
    message = entry.get()
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "Server: " + message + "\n", 'server')
    chat_log.config(state=tk.DISABLED)
    entry.delete(0, tk.END)
    broadcast_message(message, None)


host = '10.100.102.15'
port = 1234
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


root = tk.Tk()
root.title("Server Chat Simulator")

bg_color = "#2e2e2e"
fg_color = "#00ff00"
font_name = "Helvetica"
header_font = (font_name, 20, 'bold')
text_font = (font_name, 12)

header = tk.Label(root, text="Server Chat Simulator", bg=fg_color, fg="white", font=header_font)
header.pack(fill=tk.X)

chat_log = tk.Text(root, state=tk.DISABLED, width=50, height=20, bg=bg_color, fg="white", font=text_font)
chat_log.tag_configure('server', foreground=fg_color)
chat_log.tag_configure('client', foreground="white")
chat_log.pack(padx=10, pady=10)

entry = tk.Entry(root, width=40, bg="white", fg="black", font=text_font)
entry.pack(side=tk.LEFT, padx=(10, 0), pady=(0, 10))

send_button = tk.Button(root, text="Send", command=send_message, bg=fg_color, fg="white", font=text_font)
send_button.pack(side=tk.RIGHT, padx=(0, 10), pady=(0, 10))

root.configure(bg=bg_color)

server_thread = threading.Thread(target=start_server)
server_thread.daemon = True
server_thread.start()

root.mainloop()
