#################################################
# Ejemplos de uso de tipos de datos en python	#
# Redes Multimedia 				#
# 2014-2015					#
# Javier Ramos de Santiago			#
# javier.ramos@uam.es			#
#################################################

import struct
import threading
import time

class hilo(threading.Thread):
	def __init__(self,parametro1,parametro2): 
		threading.Thread.__init__(self)
		self.param1=parametro1
		self.param2=parametro2
		self.seguir=True
	

	def run(self):
		while self.seguir==True:
			print ("parametros: ",self.param1,self.param2)
			time.sleep(5)
	def parar(self):
		self.seguir=False		
			
		

def suma(param1, param2=2) : 

    return param1+param2


a=2
print("Ejemplo de IF")
if a==1:
    print ("A vale 1")
else:
    pass

input("Pulsa Enter para continuar")




print("Ejemplo de bucle for con funcion range")
for i in range(1,10,2):
    print (str(i)+"\n")
a=0
input("Pulsa Enter para continuar") 




print("Ejemplo de bucle while");
while a<10:
    print (str(a)+"\n")
    a=a+2;
input("Pulsa Enter para continuar") 

print("Ejemplo de uso de funcion")
print(suma(1,7))

input("Pulsa Enter para continuar")



print("Ejemplo de uso de listas")
a=[1,2,3,4,5]
print ("la lista es: "+str(a))
longitud=len(a)
print ("La longitud de la lista es: "+ str(longitud))
print("El primer elemento es "+str(a[0]))
a[0]=0
print("cambiamos el primer elemento y ahora es "+str(a[0]))
print("El ultimo elemento es "+str(a[-1]))
print("Los elementos de la posicion 2 a la 4 son "+str(a[1:4]))
a=a[3:]
print("Quitamos los elementos 1 a 3 y la nueva lista es "+str(a))
input("Pulsa Enter para continuar") 



print("Ejemplo de uso de tuplas")
tupla=(1,2,3,4,5)
print ("la tupla es: "+str(tupla))
longitud=len(tupla)
print ("La longitud de la tupla es: "+ str(longitud))
print("El primer elemento es "+str(tupla[0]))
print("El ultimo elemento es "+str(tupla[-1]))
print("Los elementos de la posicion 2 a la 4 son "+str(tupla[1:4]))
tupla=tupla[3:]
#tupla[0]=0 las tuplas no pueden ser modificadas
print("intentamos cambiar el primer elemento pero no se puede")
input("Pulsa Enter para continuar") 



print("Ejemplo de uso de conjuntos")
colores1={"Rojo","Azul","Verde"}
colores2={"Amarillo","Negro"}
print("El conjunto 1 es "+str(colores1));
print("El conjunto 2es "+str(colores2));
print("Esta el color rojo en el conjunto 1?")
print("Rojo" in colores1)
print("Esta el color amarillo en el conjunto 1?")
print("Amarillo" in colores1)
colores=colores1.union(colores2);
print("Si unimos los 2 conjuntos tenemos el conjunto "+str(colores))
input("Pulsa Enter para continuar") 



print("Ejemplo de uso de diccionarios")
a={"Juan":1,"Pedro":2,"Luis":34}
print ("El diccionario es: "+str(a))
print ("Que valor numerico tiene Juan?")
print (a["Juan"])
print ("Existe el usuario Antonio?")
print ("Antonio" in a)

input("Pulsa Enter para continuar") 

print("Ejemplo de uso de pack/unpack")

numero1=0
numero2=1
numero3=2
mensaje=struct.pack('!HHII',0x8014,numero1,numero2,numero3)
print ("El mensaje empaquetado es "+str(mensaje))


aux=struct.unpack('!HHII',mensaje)

print("Constante: "+str(hex(aux[0]))+" Numero1: "+str(aux[1])+" Numero2: "+str(aux[2])+" Numero3: "+str(aux[3]))
input("Pulsa Enter para continuar") 
input("Ejemplo de uso de hilos")
h=hilo("Parametro 1","Parametro 2")
#Llamando a este metodo inciamos la ejecucion del hilo y se ejecuta el codigo contenido en el metodo run
h.start()
time.sleep(20)
#Llamando a este metodo le decimos a la clase hilo que pare su ejecucin
h.parar()
#Con esta instruccion esperamos a que acabe el hilo
h.join() 



input("Pulse Enter para finalizar") 





