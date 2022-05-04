import socket

PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '/exit'
SERVER = '192.168.1.4'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    client.send(message)
    # print(client.recv(2048).decode(FORMAT))

while True:
    msg = input()
    if(msg == DISCONNECT_MESSAGE):
        send('user: ' + SERVER + ' leaves!')
        break
    else:
        send(msg)

send(DISCONNECT_MESSAGE)