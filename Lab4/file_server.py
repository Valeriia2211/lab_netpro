import socket

HOST = '127.0.0.1'
PORT = 65433

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print("File server started, waiting for client...")

    conn, addr = s.accept()
    with conn:
        print("Connected by", addr)
        with open("received.txt", "wb") as f:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                f.write(data)

print("File received and saved")
