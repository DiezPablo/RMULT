# -*- coding: windows-1252 -*-
import socket
import time
import struct

# Declaraci�n de variables
IP_SERVER = "127.0.0.1"
PORT_SERVER = 5004

# Se crea un socket para recibir (servidor)
sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP

sock.bind((IP_SERVER, PORT_SERVER))

while True:
	# Se pone el servidor a la escucha
    data, addr = sock.recvfrom(2048) # Tamaño del buffer de recepci�n
    cabecera = struct.unpack('!HHII',data[0:12])
    print(cabecera[1])
    msg = data[12:]
    print(msg.decode())
    #print(data.decode())
    sock.sendto(data, addr)
