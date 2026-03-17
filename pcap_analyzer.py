from scapy.all import rdpcap
import sys

from detectors import PortScanDetector, CredentialDetector, DNSDetector
from report import Report
from utils import summarize_packets, current_time


def main():

    # check command usage
    if len(sys.argv) != 2:
        print("Usage: python pcap_analyzer.py <pcap_file>")
        return

    pcap_file = sys.argv[1]

    print(f"\nAnalyzing {pcap_file}...\n")

    # read packets
    packets = rdpcap(pcap_file)

    # initialize detectors
    portscan = PortScanDetector()
    creds = CredentialDetector()
    dns = DNSDetector()

    # process packets
    for pkt in packets:
        portscan.process(pkt)
        creds.process(pkt)
        dns.process(pkt)

    # create report
    report = Report()

    report.add("===== PCAP SECURITY ANALYSIS REPORT =====")
    report.add("File:", pcap_file)
    report.add("Analysis Time:", current_time())
    report.add("Total Packets:", len(packets))
    report.add("")

    # detect port scans
    portscan_results = portscan.detect()

    for result in portscan_results:
        report.add("[HIGH] Port Scan Detected")
        report.add("Source:", result["source"])
        report.add("Scanned", result["ports"], "ports in", result["time"], "seconds")
        report.add("")

    # detect credentials
    cred_results = creds.detect()

    for cred in cred_results:
        report.add("[CRITICAL] Cleartext Credentials Found")
        report.add(cred)
        report.add("")

    # detect suspicious DNS
    dns_results = dns.detect()

    for result in dns_results:
        report.add("[MEDIUM] Suspicious DNS Activity")
        report.add("Domain:", result["domain"])
        report.add("Queried", result["count"], "times")
        report.add("")

    # traffic summary
    stats = summarize_packets(packets)

    summary_lines = []

    sorted_stats = sorted(stats.items(), key=lambda x: x[1], reverse=True)

    for ip, count in sorted_stats[:5]:
        summary_lines.append(f"{ip} -> {count} packets")

    report.add_summary(summary_lines)

    # print report
    report.print()

    # save report
    report.save()


if __name__ == "__main__":
    main()