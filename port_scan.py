import socket
from IPy import IP

banners_list = []
open_ports = []

#port = input("[+] Target Port: ")

def multi_Scan(ip_addr_stripped,port_nums):
    print(f"[_0] Scanning Target {ip_addr_stripped}")
    for port in range(0,port_nums):
        port_scanner(ip_addr_stripped,port)
    banners_list = []
    open_ports = []


def port_scanner(ip_address,port,timeout):
    global banners_list
    global open_ports

    try:
        sock = socket.socket()
        sock.settimeout(timeout)
        sock.connect((ip_address,port))

        try:
            banner = sock.recv(1024).decode().strip("\n").strip("\r")
            print(f"[+] Open Port With Banner [{port}] {banner}")
            banners_list.append(banner)
            open_ports.append(port)

        except:
            print(f"[>+<] Port {port} is Open")
            open_ports.append(port)
            banners_list.append(" ")

    except:
        pass


def main(ip_addr_stripped,target_port_scan_ammount,timeout):
    
    ip_address = ip_addr_stripped

    if ',' in ip_address:
        for ip_addr_stripped in ip_address.split(','):
            multi_Scan(ip_addr_stripped.strip(" "),target_port_scan_ammount)

    else:
        print("-------- Open Ports --------")
        for port in range(0,int(target_port_scan_ammount)):
            port_scanner(ip_address,port,timeout)

        print("Scan Finished")
