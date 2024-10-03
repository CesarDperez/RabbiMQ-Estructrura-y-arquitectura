import pika
import json

# Conexión a RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declarar el exchange de tipo fanout
channel.exchange_declare(exchange='cobro_facturacion', exchange_type='fanout')

# Crear una cola temporal
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

# Enlazar la cola al exchange
channel.queue_bind(exchange='cobro_facturacion', queue=queue_name)

print(' [*] Esperando datos de cobro. Para salir presiona CTRL+C')

def callback(ch, method, properties, body):
    datos = json.loads(body)
    print(f" [x] Datos recibidos: {datos}")
    # Aquí calcularías la factura y la enviarías al usuario

# Consumir los mensajes
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
