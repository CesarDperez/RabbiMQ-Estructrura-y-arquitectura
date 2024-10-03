import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='optimizacion_espacio', exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='optimizacion_espacio', queue=queue_name)

def callback(ch, method, properties, body):
    ocupacion = json.loads(body)
    print(f" [x] Recibido: {ocupacion}")

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
channel.start_consuming()
