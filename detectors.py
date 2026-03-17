from scapy.all import IP, TCP, DNSQR, Raw
from collections import defaultdict

SUSPICIOUS_KEYWORDS = ["malware", "botnet", "c2", ".xyz"]


class PortScanDetector:
    def __init__(self):
        self.scan_data = defaultdict(list)

    def process(self, pkt):
        if pkt.haslayer(IP) and pkt.haslayer(TCP):
            src = pkt[IP].src
            dport = pkt[TCP].dport
            timestamp = pkt.time

            self.scan_data[src].append((dport, timestamp))

    def detect(self):
        alerts = []

        for src, entries in self.scan_data.items():
            ports = set([p for p, t in entries])

            if len(ports) > 50:
                first = entries[0][1]
                last = entries[-1][1]
                duration = round(last - first, 2)

                alerts.append({
                    "source": src,
                    "ports": len(ports),
                    "time": duration
                })

        return alerts


class CredentialDetector:
    def __init__(self):
        self.credentials = []

    def process(self, pkt):
        if pkt.haslayer(Raw):
            try:
                payload = pkt[Raw].load.decode(errors="ignore")

                if "USER" in payload or "PASS" in payload or "Authorization:" in payload:
                    self.credentials.append(payload.strip())

            except:
                pass

    def detect(self):
        return self.credentials


class DNSDetector:
    def __init__(self):
        self.domains = defaultdict(int)

    def process(self, pkt):
        if pkt.haslayer(DNSQR):
            try:
                domain = pkt[DNSQR].qname.decode()
                self.domains[domain] += 1
            except:
                pass

    def detect(self):
        suspicious = []

        for domain, count in self.domains.items():
            if count > 20 or any(k in domain for k in SUSPICIOUS_KEYWORDS):
                suspicious.append({
                    "domain": domain,
                    "count": count
                })

        return suspicious