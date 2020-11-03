# IPv4-Packet-Crafting
The client crafts an ipv4 packet and sends it to the server via raw socket.

## Overview
I observed some blogs on how scapy, a third party packet crafting library works and tried to create a similar IPv4 structure in python to send to  the destination using a raw socket.   
## Client Side 
On the client side I crafted an ipv4 packet by packing all  required fields of ipv4 header in a struct and sending it to the  destination address using a raw socket and raw protocol.   
## Server-Side 
On the server side we use a raw socket to receive the packet  sent by the client side. 
