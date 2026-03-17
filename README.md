# Network Traffic Analyzer

## Project Overview

The Network Traffic Analyzer is a modular Python-based security analysis framework designed to inspect captured network traffic and identify indicators of malicious or suspicious activity.

The system processes packet capture (PCAP) datasets and applies multiple behavioural detection modules to uncover potential reconnaissance attempts, insecure credential transmission, and abnormal DNS communication patterns.

This project simulates the workflow of a network security analyst performing post-incident traffic investigation in enterprise environments.

It demonstrates applied knowledge of packet structures, traffic pattern analysis, and automated threat detection logic.


## Core Objectives

The project aims to replicate real investigative processes used in:

* Security Operations Centers (SOC)
* Digital Forensics and Incident Response (DFIR) teams
* Network intrusion detection research
* Malware communication analysis

By transforming raw packet captures into structured intelligence reports.


## Key Capabilities

* Detection of high-frequency TCP port scanning behaviour
* Identification of plaintext authentication credentials within traffic streams
* Analysis of DNS queries to detect potential command-and-control communication
* Automated traffic summarization and host activity profiling
* Modular detector architecture enabling extensibility
* Generation of structured forensic investigation reports
* Simulation of realistic malicious traffic for controlled testing

## Project Architecture
```
network-traffic-analyzer/
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

* Efficient packet iteration using Scapy packet reader
* Lightweight memory footprint suitable for local analysis environments
* Detection logic designed for clarity and extensibility
* Fast report generation even on large traffic datasets


## Security and Ethical Usage

This project is intended strictly for:

* Cybersecurity education
* Network defense training
* Digital forensics research
* Security tool development practice

It must only be used on authorized datasets and controlled laboratory environments.


## Learning Outcomes Demonstrated

Through this project the following competencies are showcased:

* Network protocol inspection
* Threat behaviour modeling
* Packet-level forensic reasoning
* Secure system analysis mindset
* Modular cybersecurity tool engineering
* Traffic intelligence extraction techniques


## Author

Developed as part of a practical cybersecurity engineering initiative focused on network threat detection and incident analysis skills.


## License

This project is released for academic and research use.
Users are responsible for ensuring ethical and lawful application.
