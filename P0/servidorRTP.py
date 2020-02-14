# -*- coding: utf-8 -*-
import socket
import time
import struct

# Declaracion de variables
IP_SERVER = "127.0.0.1"
PORT_SERVER = 5004
SSRC_id = 2
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
    print("Mensaje recibido: "+str(msg.decode()))
    # Enviamos la cabecera RTP y un mensaje de vuelta para dar confirmacion de que se ha recibido el mensaje, no
    # se incrementa el numero de secuencia en este caso, ya que es una confirmacion
    entrada = input("Introduce el mensaje: ")
    MESSAGE = str.encode(entrada) # Los mensajes son arrays de bytes, no strings
    tenvio = time.time()
    # Construccion cabecera RTP
    cabecera = struct.pack("!HHII", 0x8014, cabecera[3], int(tenvio), SSRC_id)
    # Construcción del mensaje que enviamos al servidor
    data_envio = cabecera +MESSAGE
    sock.sendto(data_envio, addr)

print("Se finalizo la conexión ...")
