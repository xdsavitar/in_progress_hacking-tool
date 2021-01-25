import socket
from IPy import IP
import tool_main

banners_list = []
open_ports = []

#port = input("[+] Target Port: ")

def multi_Scan(ip_addr_stripped,port_nums):
    print(f"[_0] Scanning Target {ip_addr_stripped}")
    for port in range(0,port_nums):
        port_scanner(ip_addr_stripped,port)
    banners_list = []
    open_ports = []


def port_scanner(ip_address,port,timeout,arg2):
    global banners_list
    global open_ports

    try:
        sock = socket.socket()
        sock.settimeout(timeout)
        sock.connect((ip_address,port))

        try:
            banner = sock.recv(1024).decode().strip("\n").strip("\r")
            message = (f"[+] Open Port With Banner [{port}] {banner}")
            print(f"[+] Open Port With Banner [{port}] {banner}")
            banners_list.append(banner)
            open_ports.append(port)
            tool_main.write_port_logs(message)

        except:
            message = (f"[>+<] Port {port} is Open")
            print(f"[>+<] Port {port} is Open")
            open_ports.append(port)
            banners_list.append(" ")
            tool_main.write_port_logs(message)

    except:
        pass


def main(ip_addr_stripped,target_port_scan_ammount,timeout,arg2):
    
    ip_address = ip_addr_stripped

    if ',' in ip_address:
        for ip_addr_stripped in ip_address.split(','):
            multi_Scan(ip_addr_stripped.strip(" "),target_port_scan_ammount)

    else:
        print("-------- Open Ports --------")
        for port in range(0,int(target_port_scan_ammount)):
            port_scanner(ip_address,port,timeout,arg2)


        print("Scan Finished")
