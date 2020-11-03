import socket
import struct

# ip and port for serer
ip = '127.0.0.1'
port = 8080

# Breate a raw socket
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
# Bind socket to ip and port
s.bind((ip, port))
print('Server Up')

while True:
    print('Waiting for connection ...')
    # Recieve any incoming connection
    rec_packet, addr = s.recvfrom(1024)
    print('Incoming Connection Detected')
    print(f'Packet Recieved from: {addr[0]}')
