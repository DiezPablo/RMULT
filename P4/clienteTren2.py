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
ETH_HDR_SIZE=14+4+8 # MAC header + CRC + Preamble
IP_HDR_SIZE=20
UDP_HDR_SIZE=8
RTP_HDR_SIZE=12

B_MASK=0xFFFFFFFF
DECENASMICROSECS=100000

if __name__ == "__main__":
	if len(sys.argv)<5 or len(sys.argv)>6:
		print ('Error en los argumentos:\npython clienteTren.py ip_destino puerto_destino longitud_tren longitud_datos [Tasa limitacion (Kb/s)]\n')
		exit(-1)
	
	dstIP=sys.argv[1]
	dstPort=int(sys.argv[2])
	addr=(dstIP,dstPort)
	trainLength=int(sys.argv[3])
	dataLength=int(sys.argv[4])
	waitTime=0

	totalLength=dataLength+IP_HDR_SIZE+UDP_HDR_SIZE+RTP_HDR_SIZE
	if dstIP!="127.0.0.1":
		totalLength+=ETH_HDR_SIZE
	
	if dataLength+IP_HDR_SIZE+UDP_HDR_SIZE+RTP_HDR_SIZE>MAX_ETHERNET_DATA or dataLength+IP_HDR_SIZE+UDP_HDR_SIZE+RTP_HDR_SIZE<MIN_ETHERNET_DATA :
		# Se controla si la trama sería inferior al tamaño minimo, o bien tan grande que habría que fragmentarla, estropeando la medida
		print('Tamaño de datos incorrecto')
		exit(0)

	if(len(sys.argv)==6):
		tasaKb=float(sys.argv[5])
		waitTime=(totalLength*8)/(tasaKb*1000)

	sock_send= socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
	#generar un array de datos de longitud dataLength con el caracter 0 
	data=('0'*(dataLength)).encode()
	seq_number=0


	for i in range(0,trainLength):
		#usamos la longitud del tren como identificador de fuente. De esta manera en destino podemos saber la
		#longitud original del tren. En el campo timestamp (32bits) sólo podemos enviar segundos y 
		#centésimas de milisegundos (o decenas de microsegundos, segun se quiera ver) truncados a 32bits
		message=struct.pack('!HHII',0x8014,seq_number, int(time.time()*DECENASMICROSECS)&B_MASK,trainLength)+data
		sock_send.sendto(message,addr)
		seq_number+=1
		time.sleep(waitTime)
