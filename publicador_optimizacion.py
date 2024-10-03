import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='optimizacion_espacio', exchange_type='fanout')

ocupacion_espacio = {
    'espacio_id': 101,
    'estado': 'ocupado',
    'tiempo_ocupacion': '00:30'
}

channel.basic_publish(exchange='optimizacion_espacio', routing_key='', body=json.dumps(ocupacion_espacio))
print(f" [x] Enviado: {ocupacion_espacio}")
connection.close()
