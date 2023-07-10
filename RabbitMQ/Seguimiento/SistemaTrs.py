from pymongo import MongoClient
import pika

MONGO_URI = 'mongodb://localhost'
client = MongoClient(MONGO_URI)
db=client['bdTransaccional']
collections=db['Transferencia']

credentials = pika.PlainCredentials('pgjkovxq', '593ZEKwWxz4XWz5Lm2_bVlQB350H47Rn')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='fly.rmq.cloudamqp.com',credentials=credentials,virtual_host='pgjkovxq'))
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

channel.basic_consume(on_message_callback=recepcion, queue='Usuario1', auto_ack=False)
channel.start_consuming()