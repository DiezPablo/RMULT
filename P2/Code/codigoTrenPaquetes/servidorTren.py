######################
#	servidorTren.py  #
#	Prácticas RM     #
######################


import sys
import socket
import struct
import time

MAX_ETHERNET_DATA=1500
MIN_ETHERNET_DATA=46
ETH_HDR_SIZE=14+4+8+12 # Cabecera Ethernet + CRC + Preambulo + Interframe gap
IP_HDR_SIZE=20
UDP_HDR_SIZE=8
RTP_HDR_SIZE=12

MAX_WAIT_TIME=8
MAX_BUFFER=100000000

packet_list=[]
B_MASK=0xFFFFFFFF
DECENASMICROSECS=100000

if __name__ == "__main__":
	if len(sys.argv)!=3:
		print ('Error en los argumentos:\npython3 servidorTren.py ip_escucha puerto_escucha\n')
		exit(-1)

	ipListen=sys.argv[1]
	portListen=int(sys.argv[2])

	sock_listen = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
	sock_listen.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF,MAX_BUFFER)
	sock_listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock_listen.bind((ipListen,portListen))
	sock_listen.settimeout(MAX_WAIT_TIME)
	
	#Recibimos los paquetes y salimos del bucle cuando no se reciban paquetes en MAX_WAIT_TIME segundos
	while True:
		try:
			data, addr = sock_listen.recvfrom(2048)
			#Para cada paquete recibido añadimos a la lista de paquetes
			#una tupla que contiene los datos del paquete y el tiempo en que 
			#se recibió dicho paquete
			packet_list.append((data,time.time()))

		except socket.timeout:
			break

	npackets=0
	for packet in packet_list:
		#Para cada paquete recibido extraemos de la cabecera
		#cada uno de los campos necesarios para hacer los cálculos

		data=packet[0]
		header=struct.unpack('!HHII',data[0:12])
		seq_number=header[1]
		send_time_trunc=header[2]
		trainLength=header[3]
		#ATENCIÓN: El tiempo de recepción está en formato: segundos.microsegundos
		#Usar este tiempo para calcular los anchos de banda
		reception_time=packet[1]
		npackets+=1
		#Truncamos el tiempo de recepción a centésimas de milisegundos 
		#(o decenas de microsegundos, segun se quiera ver) y 32 bits
		#para poder calcular el OWD en la misma base en que está el tiempo
		#de envío del paquete
		reception_time_trunc=int(reception_time*DECENASMICROSECS)&B_MASK

		print ('Retardo instantaneo en un sentido (s): ',(reception_time_trunc-send_time_trunc)/DECENASMICROSECS)
		###########################PRÁCTICA##############################################
		#                                                                               #
		# Añadir cálculos necesarios para obtener ancho de banda (instantáneo,medio,    #
		# máximo,mínimo) retaro en un sentido (instantáneo, medio, máximo y mínimo)     #
		# ATENCIÓN: los tiempos truncados están en centésimas de milisegundos           # 
		#         (o decenas de microsegundos, segun se quiera ver)                     #
		# a la hora de calcular retardos se debe tener en cuenta                        #
		#################################################################################


	###########################PRÁCTICA##############################################
	#                                                                               #
	# Añadir cálculos necesarios para obtener pérdida de paquetes y variación del   #
	# retardo                                                                       #
	#################################################################################
	packetLoss=0
	print('Perdida de paquetes: ',packetLoss)
	jitter=0 
	print('Variación del retardo: ',jitter)
	#################################################################################




