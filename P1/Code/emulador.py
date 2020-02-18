import sys
import socket
import random
import time

def main():

	if len(sys.argv) != 4:
		print("Error al introducir los parametros del programa.")
		print("Parametros a introducir en el programa:")
		print("\t1. Porcentaje de perdidas de paquetes.")
		print("\t2. Mínimo tiempo de espera entre paquetes en milisegundos.")
		print("\t3. Máximo tiempo de espera entre paquetes en milisegundos.")
		print("Ejemplo de ejecución del programa:")
		print("\t python3 emulador.py 127.0.01 1000 2000")

	else:
		IP_recieve = "127.0.0.1"
		PORT_recieve = 5004
		IP_client = "127.0.0.1"
		PORT_client = 5005
		loss_percentage = float(sys.argv[1])
		min_delay = int(sys.argv[2])
		max_delay = int(sys.argv[3])

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

			# Calculamos la probabilidad de que se pierda el paquete
			random_number = random.uniform(0, 1)
			if (random_number >= loss_percentage):
				time_wait = random.uniform(min_delay, max_delay)
				time_wait /= 1000
				time.sleep(time_wait)
				sock_client.sendto(data, (IP_client, PORT_client))
			else:
				print("Desechamos el paquete del emisor.")




if __name__ == "__main__":
	main()
