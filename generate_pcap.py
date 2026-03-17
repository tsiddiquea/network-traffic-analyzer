from scapy.all import IP, TCP, UDP, DNS, DNSQR, Raw, wrpcap
import random
import time

packets = []

print("Generating realistic suspicious network traffic...")

# -----------------------------
# 1. Simulate port scan attack
# -----------------------------

attacker_ip = "192.168.1.105"
target_ip = "192.168.1.1"

for port in range(20, 275):
    pkt = IP(src=attacker_ip, dst=target_ip) / TCP(dport=port, flags="S")
    packets.append(pkt)

# -----------------------------
# 2. Simulate FTP credentials
# -----------------------------

ftp_user = IP(src="192.168.1.50", dst=target_ip) / TCP(dport=21) / Raw(load="USER admin\r\n")
ftp_pass = IP(src="192.168.1.50", dst=target_ip) / TCP(dport=21) / Raw(load="PASS password123\r\n")

packets.append(ftp_user)
packets.append(ftp_pass)

# -----------------------------
# 3. Simulate HTTP credentials
# -----------------------------

http_auth = (
    "POST /login HTTP/1.1\r\n"
    "Host: example.com\r\n"
    "Authorization: Basic YWRtaW46cGFzc3dvcmQxMjM=\r\n\r\n"
)

http_pkt = IP(src="192.168.1.60", dst="93.184.216.34") / TCP(dport=80) / Raw(load=http_auth)

packets.append(http_pkt)

# -----------------------------
# 4. Simulate malware DNS beaconing
# -----------------------------

malware_domain = "malware-c2-server.xyz"

for i in range(50):
    dns = IP(src="192.168.1.200", dst="8.8.8.8") / UDP(dport=53) / DNS(
        rd=1, qd=DNSQR(qname=malware_domain)
    )
    packets.append(dns)

# -----------------------------
# Write PCAP file
# -----------------------------

wrpcap("capture.pcap", packets)

print("capture.pcap successfully generated!")
print(f"Total packets created: {len(packets)}")