import pika
import json

def callback(ch, method, properties, body):
    # Convertir el mensaje de JSON a un diccionario
    alert_message = json.loads(body)
    print(f"[x] Received alert: {alert_message}")
    
    # Lógica para manejar la alerta (ejemplo: notificación)
    handle_security_alert(alert_message)

def handle_security_alert(alert_message):
    # Aquí agregas la lógica para manejar la alerta
    # (enviar notificación a administradores, registrar en base de datos, etc.)
    print(f"Alert received! Type: {alert_message['alert_type']}, Location: {alert_message['location']}, Description: {alert_message['description']}")

# Conexión a RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declarar el intercambio y la cola
channel.exchange_declare(exchange='security_alerts', exchange_type='fanout')

# Crear una cola exclusiva y obtener su nombre
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

# Enlazar la cola al intercambio
channel.queue_bind(exchange='security_alerts', queue=queue_name)

# Configurar el callback para procesar mensajes
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print('[*] Waiting for security alerts. To exit press CTRL+C')
channel.start_consuming()