import pika

credentials = pika.PlainCredentials('pgjkovxq', '593ZEKwWxz4XWz5Lm2_bVlQB350H47Rn')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='fly.rmq.cloudamqp.com',credentials=credentials,virtual_host='pgjkovxq'))
channel = connection.channel()
def recepcion(ch, method, properties, body):
    mensaje = str(body)
    mensaje=mensaje.replace("'","")
    mensajeT=mensaje[1:]
    f = open ('Registros.txt','w')
    f.write(mensajeT)
    f.write("\n======================================")
    f.close()
    print("Fichero Actualizado")

channel.basic_consume(on_message_callback=recepcion, queue='Usuario2', auto_ack=False)
channel.start_consuming()