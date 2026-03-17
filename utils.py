from collections import defaultdict
import time

def current_time():
    return time.strftime("%Y-%m-%d %H:%M:%S")

def summarize_packets(packets):

    ip_counter = {}

    for pkt in packets:

        if pkt.haslayer("IP"):

            src = pkt["IP"].src

            if src not in ip_counter:
                ip_counter[src] = 0

            ip_counter[src] += 1

    return ip_counter