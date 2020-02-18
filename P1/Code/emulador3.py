import sys
import socket
import random
import time
import threading

def send_packet_client (sock_client, data, sigma, media, min_delay, max_delay, IP_client, PORT_client):


	time_wait = random.gauss(media, sigma)
	while time_wait > max_delay or time_wait < min_delay:
		time_wait = random.gauss(media, sigma)
	time.sleep(time_wait)
	sock_client.sendto(data, (IP_client, PORT_client))

def main():

	if len(sys.argv) != 4:
		print("Error al introducir los parametros del programa.")
		print("Parametros a introducir en el programa:")
		print("\t1. Porcentaje de perdidas de paquetes.")
		print("\t2. Mínimo tiempo de espera entre paquetes en milisegundos.")
		print("\t3. Máximo tiempo de espera entre paquetes en milisegundos.")
		print("Ejemplo de ejecución del programa:")
		print("\t python3 emulador.py 0.01 1000 2000")

	else:
		IP_recieve = "127.0.0.1"
		PORT_recieve = 5004
		IP_client = "127.0.0.1"
		PORT_client = 5005
		loss_percentage = float(sys.argv[1])
		min_delay = int(sys.argv[2])
		max_delay = int(sys.argv[3])

		media = (max_delay - min_delay)/2
		sigma = (media - min_delay)/3
		media /= 1000
		sigma /= 1000

		# Abrimos el socket de escucha
		sock_receive = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

		# Enlazamos el socket para escuchar los paquetes
		sock_receive.bind((IP_recieve,PORT_recieve))

		# Aumentamos el buffer del socket
		sock_receive.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 65535)

		# Escuchamos los paquetes
		while(True):
			# Obtenemos los paquetes que nos llegan desde el emisor
			data, addr = sock_receive.recvfrom(65535)
			thread_delay = threading.Thread(target=send_packet_client, args=(sock_client, data,sigma, media, min_delay, max_delay,IP_client, PORT_client,))

			# Regla de las tres sigmas: media +- 33sigmas
			# media = min + max/2
			# media -3sigmas = minimo
			# Si cae fuera del intervalo, volver a tirar.
			random_number = random.uniform(0, 1)
			if (random_number >= loss_percentage):
				# Comenzamos a ejecutar el hilo de envio de paquetes
				thread_delay.start()
			else:
				print("Desechamos el paquete del emisor.")




if __name__ == "__main__":
	main()
