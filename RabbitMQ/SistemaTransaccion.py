import pika



credentials = pika.PlainCredentials('knqwjfhx', 'ZpBfwYNn_nw3eBWRxcomm8HPOHSuS-Z-')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='fly.rmq.cloudamqp.com',credentials=credentials,virtual_host='knqwjfhx'))
channel = connection.channel()

def recepcion(ch, method, properties, body):
    mensaje = str(body)
    mensaje=mensaje.replace("'","") 
    mensajeT=mensaje[1:]
    tipo=mensajeT[14:19]
    if(tipo=="Inscr"):
        print("a") # DESDE AQUI GUARDA TODOS LOS MENSAJET DE TIPO INSCRIPCION EN LA BD
    elif(tipo=="Trans"):
        print("b")# DESDE AQUI GUARDA TODOS LOS MENSAJET DE TIPO TRANSFERENCIA EN LA BD

channel.basic_consume(on_message_callback=recepcion, queue='PrimerUsuario', auto_ack=False)
channel.start_consuming()