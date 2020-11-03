import socket
import struct


class modIPv4:
    """
    This class is used for creating modified ipv4 packets
    """

    # Takes source, destionation ip and port as arguments
    def __init__(self, src_ip, src_port, dst_ip, dst_port):
        self.src_ip = src_ip
        self.src_port = src_port
        self.dst_ip = dst_ip
        self.dst_port = dst_port

    # Packs the headers into a struct with user modified values
    def craft(self) -> bytes:
        packet = struct.pack(
            '!HHIIBBHHH',
            self.src_port,  # Source Port
            self.dst_port,  # Destination Port
            0,              # Sequence Number
            1,              # ACK Number
            5 << 4,         # Offset
            0,              # Flags
            8192,           # Window
            0,              # Checksum
            0,              # Urgent pointer
        )
        # returns packet in bytes
        return packet


if __name__ == '__main__':

    # Create instance of modified packet
    packet = modIPv4(
        '192.168.100.7', 8080,  # Source IP and Port
        '192.168.100.8', 8080   # Destination IP and Port
    )
    # Create a Raw Tcp Socket
    client = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    # Send the Raw crafted packet to the destination
    client.sendto(packet.craft(), (packet.dst_ip, packet.dst_port))
