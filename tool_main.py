import port_scan
import time
import random
import socket
import string
import ddos_attack
import os 
args_list = []
device_name_PIPE =  socket.gethostname()
source_ip_addr = "192.142.123.234"
called = 0 




def write_port_logs(message):
	print(message)

	with open("logs.txt",'a') as log:
		log.write(message +"\n")
		log.close()




def command_help():
	print("1.scanport --[ip] --[portammount] /**Optional**/ --[mode]")
	print("2.ddos --[ip] --[randint,static] --[maxport,none]\n")



def command_splitter(arg1,arg2):
	ip_address = arg1
	port_ammount = arg2

	port_scan.main(ip_address,port_ammount)


def call(arg1,arg2):
	ip = input("Enter ip: ").lower()
	port_ammount = input("Port Ammount: ")
	port_scan.main(ip,port_ammount,arg1,arg2)



def proccess_command(comm):
	global args_list
	if '--' in comm:
		for args in comm.split("--"):
			args_list.append(args)


		try:
			arg0 = args_list[0]
			arg1 = args_list[1]
			arg2 = args_list[2]
			arg3 = args_list[3]
			arg4 = args_list[4]
		except:


			pass



		if (str(arg0.strip(" ")) == "scanport"):

			if (arg1.strip(" ") == "ip" and arg2.strip(" ") == "portammount"):
				print(args_list)


				try:
					if (arg3.strip(" ") == "mode" and arg4.strip(" ") == "write"):
						write = True
						costum_timeout = float(input("Timeout: "))
						call(costum_timeout,write)
						args_list = []

				except UnboundLocalError:
					call(0.2)



		if (str(arg0.strip(" ")) == "help"):

			command_help()

			args_list = []

		elif (str(arg0.strip(" ")) == "cls"):

			os.system("cls")

			args_list = []




		if (str(arg0.strip(" ")) == "ddos" and (str(arg1.strip(" ")) == "static")):

			print("Called static")

			static_port = str(arg2)

			end_ip = str(arg3)

			ddos_attack.main_ddos_loop_static(static_port,end_ip)



		if (str(arg0.strip(" ")) == "ddos" and (str(arg1.strip(" ")) == "randint")):

			domain_ip = str((arg2.strip(" ")))

			randint = "randint_loop"

			ddos_attack.main_ddos_loop_random(domain_ip)

	else:
		print("You must put '--' after each command\n")

		args_list = []

def main_menu():

	while True:	

		CONSOLE_PIPE = str(input(f"{device_name_PIPE}$ "))

		proccess_command(CONSOLE_PIPE)



if __name__ == '__main__':

	main_menu()