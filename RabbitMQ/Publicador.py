import pika
import sys
from datetime import datetime

credentials = pika.PlainCredentials('knqwjfhx', 'ZpBfwYNn_nw3eBWRxcomm8HPOHSuS-Z-')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='fly.rmq.cloudamqp.com',credentials=credentials,virtual_host='knqwjfhx'))
channel = connection.channel()

eleccion= input("1. Inscripcion \n 2. Transferencia")
if(eleccion=="1"):
    Tipo="Inscripcion"
    cuentaO=input("Cuenta Origen :")
    cuentaI=input("Cuenta Inscrita :")
    cedula=input("Cedula :")
    fecha=datetime.today().strftime('%Y/%m/%d')
    mensaje="TipoOperacion: "+Tipo+"; cuentaOrigen:"+cuentaO+"; cuentaInscrita:"+cuentaI+"; CedulaTitularCuentaInscrita:"+cedula+"; fechaHoraInscripcion:"+fecha+";"
    channel.basic_publish(exchange='Dinero', routing_key='inscripcion', body=mensaje)
elif(eleccion=="2"):
    Tipo="transferencia"
    cuentaO=input("Cuenta Origen :")
    cuentaI=input("Cuenta Inscrita :")
    Monto=input("Monto :")
    fecha=datetime.today().strftime('%Y/%m/%d')
    mensaje="TipoOperacion: "+Tipo+"; cuentaOrigen:"+cuentaO+"; cuentaInscrita:"+cuentaI+"; Monto:"+Monto+"; fechaHoraInscripcion:"+fecha+";"
    channel.basic_publish(exchange='Dinero', routing_key='transferencia', body=mensaje)
    

    
print(" Se acaba de enviar :  %r" % mensaje)
connection.close()