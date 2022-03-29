import smtplib, ssl
import os
import time
import getpass

#colores
negro = '\033[30m'
rojo = '\033[31m'
verde = '\033[32m'
amarillo = '\033[33m'
azul = '\033[34m'
rosado = '\033[35m'
calipso= '\033[36m'
blanco = '\033[37m'
cierre = '\033[39m'

#script
os.system("clear")
time.sleep(2.0)
print(amarillo+"Gracias por usarlo atte RIP NETWORK"+cierre)
os.system("clear")

a = open(os.devnull,'w')


if input("\n\033[1;41;37mADVERTENCIA\033[0;m \033[1;33m¿Acepta utilizar esta herramienta con fines educativos?\033[0;m [\033[1;32my\033[0;m/\033[1;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
 os.system('clear')

print(amarillo+"Gracias por usarlo atte RIP NETWORK"+cierre)
 

if input("\n\033[1;41;37mBUZONES ESP\033[0;m \033[1;33mDesea empezar el programa para ver buzones de compañias?\033[0;m [\033[1;32my\033[0;m/\033[1;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
 os.system('clear')



print(blanco+"Movistar llama +34 609 123 123 , contraseña 1234 "+cierre)
print(blanco+"Vodafone no disponible"+cierre)
print(blanco+"Yoigo llama +34 633 633 633 , contraseña 2525 "+cierre)

print(blanco+"Este programa sigue actualizandose cada semana , para actualizarlo solo eliminalo y vuelvelo a instalar desde mi github"+cierre)
