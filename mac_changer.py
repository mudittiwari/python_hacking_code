import subprocess
import optparse
import re

def changemac(interface,new_mac):
    subprocess.call(['sudo' ,'ifconfig', interface, 'down'])
    subprocess.call(['sudo' ,'ifconfig', interface, 'hw', 'ether', new_mac])
    subprocess.call(['sudo' ,'ifconfig', interface, 'up'])
    # subprocess.call(['ifconfig'])



def parseinput():
    parser=optparse.OptionParser()
    parser.add_option('-i','--interface',dest='interface',help='interface to change the mac address')
    parser.add_option('-m','--new_mac',dest='new_mac',help='new mac address of the interface')
    (options,arguments)=parser.parse_args()
    return options

def checkoutput(options):
    ifconfigres=subprocess.check_output(["sudo", "ifconfig", "wlan0"]).decode('utf-8')
    mac=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfigres)
    # print(mac)
    if mac is None:
        print("could not read mac address")
    else:
        if mac.group(0)==options.new_mac:
            print("[+] Mac address changed successfully")
        else:
            print("[!] Mac address change unsuccessfull")



options=parseinput()
print(f"[+] changing mac address of interface {options.interface} to {options.new_mac}")
changemac(options.interface,options.new_mac)
checkoutput(options)








# subprocess.call('sudo ifconfig wlan0 down',shell=True)
# subprocess.call('sudo ifconfig wlan0 hw ether 00:22:33:44:55:66',shell=True)
# subprocess.call('sudo ifconfig wlan0 up',shell=True)
# subprocess.call('ifconfig',shell=True)