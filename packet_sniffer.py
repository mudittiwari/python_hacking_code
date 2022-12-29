import scapy.all as scapy
from scapy.layers.http import HTTPRequest,Raw

def process_sniffed_packets(packet):
    # print(packet.show())
    try:
        if packet.haslayer(HTTPRequest):
            url = packet[HTTPRequest].Host.decode() + packet[HTTPRequest].Path.decode()
            print(url)
            # print(packet.show())
            # print(packet[Raw])
            load=packet[Raw].load
            print(load.decode('utf-8'))
            # keywords=["username","user","login","password","pass"]
            # for word in keywords:
            #     if word in load:
            #         print(load)
            #         break
    except Exception as e:
        print(e)


def sniff(interface):
    scapy.sniff(iface=interface,store=False,prn=process_sniffed_packets)

sniff("wlan0")