import socket

HOST = '127.0.0.1'
PORT = 65433

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    with open("test.txt", "rb") as f:
        s.sendall(f.read())

print("File sent successfully")

