import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Server running...")

    while True:
        conn, addr = s.accept()
        with conn:
            print('Client:', addr)
            data = conn.recv(1024)
            conn.sendall(data)
