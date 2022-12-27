import scapy.all as scapy


packet=scapy.ARP(op=2,pdst="192.168.29.65",hwdst="88:b4:a6:1b:c1:ed",psrc="192.168.29.1")
