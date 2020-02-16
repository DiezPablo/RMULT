import sys
import socket
import random
import time

def main():

	if len(sys.argv) != 8:
		print("Error al introducir los parametros del programa.")
		print("Parametros a introducir en el programa:")
		print("\t1. IP del cliente que escuchamos.")
		print("\t2. Puerto del cliente que escuchamos.")
		print("\t3. IP del cliente que enviamos.")
		print("\t4. Puerto del cliente que enviamos.")
		print("\t5. Porcentaje de perdidas de paquetes.")
		print("\t6. Mínimo tiempo de espera entre paquetes en milisegundos.")
		print("\t7. Máximo tiempo de espera entre paquetes en milisegundos.")
		print("Ejemplo de ejecución del programa:")
		print("\t python3 emulador.py 127.0.0.1 5004 127.0.0.1 5005 0.01 1000 2000")

	else:
		IP_recieve = sys.argv[1]
		PORT_recieve = int(sys.argv[2])
		IP_client = sys.argv[3]
		PORT_client = int(sys.argv[4])
		loss_percentage = float(sys.argv[5])
		min_delay = int(sys.argv[6])
		max_delay = int(sys.argv[7])

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