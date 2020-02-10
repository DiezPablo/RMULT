# -*- coding: utf-8 -*-
import socket
import time
import struct

# Declaracion de variables
IP_SERVER = "127.0.0.1"
PORT_SERVER = 5004

# Se crea un socket para recibir (servidor)
sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP

sock.bind((IP_SERVER, PORT_SERVER))

while True:
	# Se pone el servidor a la escucha
    data, addr = sock.recvfrom(2048) # Tamaño del buffer de recepcion
    # Obtenemos la cabecera RTP del mensaje 
    cabecera = struct.unpack('!HHII',data[0:12])
    # Obtenemos el mensaje que ha enviado el cliente
    msg = data[12:]
    # Mostramos el mensaje
    print(">>>"+str(msg.decode()))
    # Enviamos la cabecera RTP para dar confirmacion de que se ha recibido el mensaje
    sock.sendto(data, addr)

print("Se finalizo la conexión ...")
