######################
#	clienteTren.py   #
#	Prácticas RM     #
######################

import sys
import socket
import struct
import time

MAX_ETHERNET_DATA=1500
MIN_ETHERNET_DATA=46
ETH_HDR_SIZE=14+4+8+12 # Cabecera Ethernet + CRC + Preámbulo + InterFrame gap
IP_HDR_SIZE=20
UDP_HDR_SIZE=8
RTP_HDR_SIZE=12

B_MASK=0xFFFFFFFF
DECENASMICROSECS=100000

if __name__ == "__main__":
	if len(sys.argv)!=6:
		print ('Error en los argumentos:\npython3 clienteTren.py ip_destino puerto_destino longitud_tren longitud_datos tasa_envio\n')
		exit(-1)

	dstIP=sys.argv[1]
	dstPort=int(sys.argv[2])
	addr=(dstIP,dstPort)
	trainLength=int(sys.argv[3])
	dataLength=int(sys.argv[4])
	tasa_envio = float(sys.argv[5])


	if (dstIP != "127.0.0.1" and (dataLength+IP_HDR_SIZE+UDP_HDR_SIZE+RTP_HDR_SIZE>MAX_ETHERNET_DATA or dataLength+IP_HDR_SIZE+UDP_HDR_SIZE+RTP_HDR_SIZE<MIN_ETHERNET_DATA)) or (dstIP == "127.0.0.1" and (dataLength+IP_HDR_SIZE+UDP_HDR_SIZE+RTP_HDR_SIZE>MAX_ETHERNET_DATA)):
		# Se controla si la trama sería inferior al tamaño minimo, o bien tan grande que habría que fragmentarla, estropeando la medida
		#PRACTICA : Añadir los controles de tamaño necesarios para el caso de localhost
		print('Tamaño de datos incorrecto')
		exit(0)
	sock_send= socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
	#generar un array de datos de longitud dataLength con el caracter 0
	if dstIP == "127.0.0.1":
		dataLength += IP_HDR_SIZE+UDP_HDR_SIZE+RTP_HDR_SIZE
	else:
		dataLength += IP_HDR_SIZE+UDP_HDR_SIZE+RTP_HDR_SIZE+ETH_HDR_SIZE
	data=('0'*(dataLength)).encode()
	seq_number=0
	time_wait = dataLength / tasa_envio

	for i in range(0,trainLength):
		#usamos la longitud del tren como identificador de fuente. De esta manera en destino podemos saber la
		#longitud original del tren. En el campo timestamp (32bits) sólo podemos enviar segundos y 
		#centésimas de milisegundos (o decenas de microsegundos, segun se quiera ver) truncados a 32bits
		message=struct.pack('!HHII',0x8014,seq_number, int(time.time()*DECENASMICROSECS)&B_MASK,trainLength)+data
		sock_send.sendto(message,addr)
		time.sleep(time_wait)
		seq_number+=1

