import socket
# Define the host and port
Host = "127.0.0.1"
port = 65432

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    # Data is sent
    s.sendto(b"Hello, world", (Host, port))
    # Data is received
    data, addr = s.recvfrom(1024)
    print(f"Received {data.decode('utf-8')} from {addr}")