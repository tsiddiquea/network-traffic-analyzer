# PCAP Forensics Analyzer

## Overview

The PCAP Forensics Analyzer is an advanced cybersecurity analysis tool developed to simulate real-world digital forensics and network threat investigation workflows.

This project processes packet capture (PCAP) files and performs automated detection of suspicious network behavior such as:

* Port scanning attacks
* Credential leakage in network traffic
* Suspicious DNS communication patterns
* Traffic distribution and anomaly summary

The system demonstrates applied knowledge of network security monitoring, threat detection engineering, and packet-level forensic analysis, reflecting real techniques used by Security Operations Centers (SOC) and incident response teams.


## Key Features

* Automated PCAP parsing and analysis using packet inspection
* Detection of high-frequency port scanning behavior
* Identification of plaintext credential transmission in HTTP / FTP traffic
* Monitoring of suspicious DNS query patterns linked to potential malware activity
* Network traffic summary generation
* Structured forensic report generation and export
* Modular detection architecture for extensibility
* Simulated realistic attack traffic generator


## Project Architecture
```
pcap-forensics-analyzer/
│
├── pcap_analyzer.py        → Main analysis engine
├── detectors.py            → Threat detection modules
├── generate_pcap.py        → Suspicious traffic simulator
├── report.py               → Report builder and formatter
├── utils.py                → Helper functions and packet summarization
├── report.txt              → Generated forensic analysis output
└── README.md
```


## Detection Capabilities

### Port Scan Detection

The analyzer tracks connection attempts across multiple destination ports within short time windows to identify reconnaissance activities commonly performed during the early stages of cyber attacks.

### Credential Exposure Detection

The tool inspects packet payloads to detect potential transmission of sensitive authentication data such as:

* FTP login credentials
* HTTP authorization headers
* Plaintext password patterns

### Suspicious DNS Activity Monitoring

Repeated DNS queries to domains containing suspicious keywords are flagged as potential command-and-control (C2) beaconing behavior.

### Traffic Pattern Analysis

Network communication patterns are summarized to provide:

* Top talker IP addresses
* Packet distribution statistics
* Behavioral indicators of compromised hosts


## Technologies Used

* Python
* Scapy (packet manipulation and analysis)
* Standard networking protocols (TCP, UDP, DNS, HTTP)
* File-based forensic reporting


## How It Works

1. Suspicious network traffic is generated using the simulator module.
2. The analyzer reads packets from a PCAP file.
3. Detection engines process packets independently.
4. Indicators of compromise are collected.
5. A structured forensic report is generated.


## Usage

### Generate Test Traffic
```
python generate_pcap.py
```

This will create a realistic PCAP file containing simulated:

* Port scanning behavior
* Credential leakage
* Suspicious DNS queries

### Analyze the PCAP File
```
python pcap_analyzer.py capture.pcap
```


## Example Output
```
===== PCAP SECURITY ANALYSIS REPORT =====
Total Packets: 308

[HIGH] Port Scan Detected
Source: 192.168.1.105
Scanned 255 ports in 0.83 seconds

[CRITICAL] Cleartext Credentials Found
USER admin
PASS password123

[MEDIUM] Suspicious DNS Activity
Domain: malware-c2-server.xyz
Queried 50 times

----- Traffic Summary -----
192.168.1.105 → 255 packets
192.168.1.200 → 50 packets
```


## Performance Characteristics

* Efficient packet processing pipeline
* Lightweight memory footprint suitable for local forensic analysis
* Modular detection design enables scaling
* Fast execution on medium-size PCAP datasets


## Security & Ethical Use

This project is designed strictly for:

* Cybersecurity education
* Digital forensics practice
* Threat detection research
* Defensive security engineering learning

It must be used only in authorized environments and controlled lab settings.


## Learning Outcomes

This project demonstrates strong competencies in:

* Network packet analysis
* Threat hunting methodology
* Digital forensic workflow design
* Security detection engineering
* Python-based cybersecurity tool development
* Realistic attack simulation techniques


## Author

Developed as part of a practical cybersecurity research initiative focused on building real-world defensive security tools and analysis frameworks.


## License

This project is released for educational and research purposes.
Users are responsible for ethical and lawful usage.
