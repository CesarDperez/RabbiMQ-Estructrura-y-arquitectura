import pika
import json

# Conexión a RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declarar el exchange de tipo fanout
channel.exchange_declare(exchange='cobro_facturacion', exchange_type='fanout')

# Simulación de datos de entrada/salida
datos_vehiculo = {
    'matricula': 'ABC123',
    'hora_entrada': '08:00',
    'hora_salida': '12:00'
}

# Enviar los datos al exchange
channel.basic_publish(exchange='cobro_facturacion',
                      routing_key='',
                      body=json.dumps(datos_vehiculo))

print(f" [x] Datos enviados: {datos_vehiculo}")
connection.close()
