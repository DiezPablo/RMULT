# -*- coding: windows-1252 -*-
import socket
import time
import struct
# Cabecera RTP
# P = 0
# X = 0
# Version 2
# timestamp = entero de 32 bits del time.time()
# Identificador unico para toda la conexion
# Debajo todo la informacion

# Declaracion de variables
IP = "127.0.0.1"
PORT = 5004
SEQ = 0
SSRC_id = 1
print ("Direccion IP de destino:", IP)
print ("Puerto UDP de destino:", PORT)


# Se crea un socket
sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP

# Se coge el tiempo antes de enviar
while(1):
    tenvio=time.time()
    entrada = input("Introduce el mensaje: ")
    MESSAGE = str.encode(entrada) # Los mensajes son arrays de bytes, no strings

    # Construccion cabecera RTP
    cabecera = struct.pack("!HHII", 0x8014,SEQ, int(tenvio), SSRC_id)
    data_envio = cabecera +MESSAGE
    print(data_envio)
    # Se envia el mensaje al destino
    sock.sendto(data_envio, (IP, PORT))
    SEQ += 1

    # Se espera la respuesta
    data, addr = sock.recvfrom(2048)
    # Se calcula el RTT
    rtt = time.time()-tenvio

    # Se comprueba la respuesta
    if data==data_envio:
    	print ("Mensaje devuelto correctamente")
    	print ("RTT", rtt)
    else:
    	print ("No volvio el mensaje correctamente")

print("Se finaliza la conexion...")
