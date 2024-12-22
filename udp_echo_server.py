import socket
# Define the host and port
Host = "127.0.0.1"
port = 65432

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((Host, port))
    print(f"Server listening on {Host}:{port}")

    while True:
        data, addr = s.recvfrom(1024)
        print(f"Connected by {addr}")
        if not data:
            break
        s.sendto(data, addr)