import socket
import threading

HEADER = 64
PORT = 5050
SERVER = '192.168.1.4'
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "/exit"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER, PORT))

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    while True:
        msg = conn.recv(HEADER).decode(FORMAT)
        
        if msg == DISCONNECT_MESSAGE:
            break

        print(f"[{addr}] {msg}")

    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

print("[STARTING] server is starting...")
start()