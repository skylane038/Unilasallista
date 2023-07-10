import pika
import sys
from datetime import datetime

credentials = pika.PlainCredentials('pgjkovxq', '593ZEKwWxz4XWz5Lm2_bVlQB350H47Rn')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='fly.rmq.cloudamqp.com',credentials=credentials,virtual_host='pgjkovxq'))# aqui tiene que cambiar el tipo de conexion por que usted tiene que configurar su rabbit 
channel = connection.channel()

eleccion= input("1. Inscripcion \n 2. Transferencia")
if(eleccion=="1"):
    Tipo="Inscripcion"
    cuentaO=input("Cuenta Origen :")
    cuentaI=input("Cuenta Inscrita :")
    cedula=input("Cedula :")
    fecha=datetime.today().strftime('%Y/%m/%d')
    mensaje="TipoOperacion: "+Tipo+"; cuentaOrigen:"+cuentaO+"; cuentaInscrita:"+cuentaI+"; CedulaTitularCuentaInscrita:"+cedula+"; fechaHoraInscripcion:"+fecha+";"
    channel.basic_publish(exchange='Flujodinero', routing_key='Inscripcion', body=mensaje)
elif(eleccion=="2"):
    Tipo="Transferencia"
    cuentaO=input("Cuenta Origen :")
    cuentaI=input("Cuenta Inscrita :")
    Monto=input("Monto :")
    fecha=datetime.today().strftime('%Y/%m/%d')
    mensaje="TipoOperacion: "+Tipo+"; cuentaOrigen:"+cuentaO+"; cuentaInscrita:"+cuentaI+"; Monto:"+Monto+"; fechaHoraInscripcion:"+fecha+";"
    channel.basic_publish(exchange='Flujodinero', routing_key='Transferencia', body=mensaje)
    #EN LOS EXCHANGE TIENE QUE CAMBIARLO A EL NOMBRE DEL EXCHANGE QUE USTED NOMBRO EN EL RABBIT

    
print(" Se acaba de enviar :  %r" % mensaje)
connection.close()