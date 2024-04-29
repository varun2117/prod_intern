import scapy.all as scapy
import os
import sys

# Function to sniff packets and analyze them
def sniff_packets(interface):
    scapy.sniff(iface=interface, store=False, prn=process_packet)

# Function to process each captured packet
def process_packet(packet):
    if packet.haslayer(scapy.IP):
        ip_src = packet[scapy.IP].src
        ip_dst = packet[scapy.IP].dst
        protocol = packet[scapy.IP].proto
        payload = packet[scapy.Raw].load if packet.haslayer(scapy.Raw) else None

        print(f"Source IP: {ip_src}, Destination IP: {ip_dst}, Protocol: {protocol}, Payload: {payload}")

# Start capturing packets on the specified interface
interface = "eth0"  # Replace "eth0" with your network interface
# Run the script with sudo
os.system(f"sudo python3 {sys.argv[0]} {interface}")
