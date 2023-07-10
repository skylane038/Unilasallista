import pika

credentials = pika.PlainCredentials('knqwjfhx', 'ZpBfwYNn_nw3eBWRxcomm8HPOHSuS-Z-')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='fly.rmq.cloudamqp.com',credentials=credentials,virtual_host='knqwjfhx'))
channel = connection.channel()
def recepcion(ch, method, properties, body): # Metodo que Recibe el mensaje de la cola 
    mensaje = str(body) # formato body a formato string 
    mensaje=mensaje.replace("'","")
    mensajeT=mensaje[1:]
    f = open ('Registros.txt','w')
    f.write(mensajeT)
    f.write("\n======================================")
    f.close()
    print("Archivo Creado")

channel.basic_consume(on_message_callback=recepcion, queue='SegundoUsuario', auto_ack=False)
channel.start_consuming()