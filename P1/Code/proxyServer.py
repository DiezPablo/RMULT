# -*- coding: utf-8 -*-
import socket
import time
import struct
import sys
import random
# Este programa se ejecuta con 7 parametros
#   1. Porcentaje perdida
#   2. Retardo minimo en ms
#   3. Retardo máximo en ms


if len(sys.argv) != 4:
    print("El programa se ejecuta con los siguientes parametros: python proxyServer.py <porcentaje_pérdida> <retardo_mínimo_en_ms> <retardo_máximo_en_ms>")
    exit()
# Creamos unas variables para almacenar todos los datos que mete el usuario por pantalla
dir_listen = "127.0.0.1" 
port_listen = 5004
dir_destination = "127.0.0.1"
port_destination = 5005
loss_percentage = sys.argv[1]
min_delay = sys.argv[2]
max_delay = sys.argv[3]

# Se crea un socket para recibir (servidor)
sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP

# Hacemos el bind en la direccion de escucha del servidor
sock.bind((dir_listen, port_listen))

# Recibimos paquetes
while True:
    data, addr = sock.recvfrom(2048) # Tamaño del buffer de recepcion
    print(data)
    # Generar un numero aleatorio para ver si el paquete se tira
    random_number = random.uniform(0,1)
    print(random_number)
    if(random_number >= loss_percentage):
        wait_time = random.uniform(min_delay, max_delay)
        time.sleep(wait_time)

        # Reenviamos al receptor el paquete
        sock.sendto(data,(dir_destination, port_destination))
        print("Envio paquete")

sock.close()    
