import scapy.all as scapy
import optparse

def parseinput():
    parser=optparse.OptionParser()
    parser.add_option('-t','--target',dest='target',help='target network ip adress')
    (options,arguments)=parser.parse_args()
    return options


def scan(ip):
    arp_request=scapy.ARP(pdst=ip)
    broadcast=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    final_arp=broadcast/arp_request
    answer,unanswer=scapy.srp(final_arp,timeout=1,verbose=False)
    clients=[]
    for item in answer:
        client={'ip':item[1].psrc,'mac':item[1].hwsrc}
        clients.append(client)
    return clients


def printclients(clients):
    print("IP\t\t\tMAC Address")
    for client in clients:
        print(client['ip']+'\t\t'+client['mac'])


options=parseinput()

clients=scan(options.target)
printclients(clients)