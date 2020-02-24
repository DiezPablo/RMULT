import sys
import socket
import random
import time
import threading

def send_packet_client (sock_client, data,min_delay, max_delay, IP_client, PORT_client):
	time_wait = random.uniform(min_delay, max_delay)
	time_wait /= 1000
	time.sleep(time_wait)
	sock_client.sendto(data, (IP_client, PORT_client))

def main():

	if len(sys.argv) != 8:
		print("Error al introducir los parametros del programa.")
		print("Parametros a introducir en el programa:")
		print("\t1. IP del emisor.")
		print("\t2. Puerto del emisor.")
		print("\t3. IP del receptor.")
		print("\t4. Puerto del receptor.")
		print("\t5. Mínimo tiempo de espera entre paquetes en milisegundos.")
		print("\t6. Máximo tiempo de espera entre paquetes en milisegundos.")
		print("\t7. Máximo tiempo de espera entre paquetes en milisegundos.")
		print("Ejemplo de ejecución del programa:")
		print("\t python3 emulador.py 127.0.0.1 5004 127.0.0.1 5005 0 1000")

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
			thread_delay = threading.Thread(target=send_packet_client, args=(sock_client, data, min_delay, max_delay, IP_client, PORT_client,))

			# Calculamos la probabilidad de que se pierda el paquete
			random_number = random.uniform(0, 1)
			if (random_number >= loss_percentage):
				# Comenzamos a ejecutar el hilo de envio de paquetes
				thread_delay.start()
			else:
				print("Desechamos el paquete del emisor.")




if __name__ == "__main__":
	main()
