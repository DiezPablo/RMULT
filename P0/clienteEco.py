# -*- coding: utf-8 -*-
import socket
import time
import struct

# Declaracion de variables
IP = "127.0.0.1"
PORT = 5004
# Número de secuencia de la cabecera RTP
SEQ = 0
# Número de Identificador de fuente de sincronización de la cabecera RTP
SSRC_id = 1

# Creamos el socket
sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP

# Bucle para poder enviar todos los mensajes que queramos
while(1):
    # Cogemos el tiempo antes de enviar el mensaje
    tenvio=time.time()
    # Obtenemos por teclado el mensaje que queremos enviar
    entrada = input("Introduce el mensaje: ")
    MESSAGE = str.encode(entrada) # Los mensajes son arrays de bytes, no strings

    # Construccion cabecera RTP
    cabecera = struct.pack("!HHII", 0x8014,SEQ, int(tenvio), SSRC_id)
    # Construcción del mensaje que enviamos al servidor
    data_envio = cabecera +MESSAGE
    # Se envia el mensaje al destino
    sock.sendto(data_envio, (IP, PORT))
    # Aumentamos el número de secuencia
    SEQ += 1
    # Se espera la respuesta
    data, addr = sock.recvfrom(2048)
    # Se calcula el RTT
    rtt = time.time()-tenvio
    # Se comprueba la respuesta
    if data==data_envio:
    	print ("Tiem de respuesta:" +str(rtt)+" milisegundos")
    else:
    	print ("No volvio el mensaje correctamente")

print("Se finaliza la conexion...")
