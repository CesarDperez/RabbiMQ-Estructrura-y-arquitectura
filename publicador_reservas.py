import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='gestion_reservas', exchange_type='fanout')

solicitud_reserva = {
    'usuario_id' : 501,
    'espacio_solicitado' : 102,
    'accion' : 'reserva'
}

channel.basic_publish(exchange='gestion_resrvas', routing_key='', body=json.dumps(solicitud_reserva))
print(f" [x] Solicitud enviada: {solicitud_reserva}")
connection.close()
