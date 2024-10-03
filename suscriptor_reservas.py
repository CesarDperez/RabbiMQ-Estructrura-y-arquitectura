import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='gestion_reservas', exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='gestion_reservas', queue=queue_name)

print(' [*] Esperando solicitudes de reserva. Para salir presiona CTRL+C')

def callback(ch, method, properties, body):
    solicitud = json.loads(body)
    print(f" [X] Solicitud recibida: {solicitud}")

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
