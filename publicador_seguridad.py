import pika
import json

def publicar_alerta_seguridad(mensaje_alerta):
    # Conexión a RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    
    # Declarar el intercambio (exchange) de tipo 'fanout'
    channel.exchange_declare(exchange='alertas_seguridad', exchange_type='fanout')
    
    # Crear un mensaje de alerta en formato JSON
    mensaje = json.dumps({
        'tipo_alerta': 'anomalia_detectada',
        'fecha_hora': mensaje_alerta['fecha_hora'],
        'ubicacion': mensaje_alerta['ubicacion'],
        'descripcion': mensaje_alerta['descripcion']
    })
    
    # Publicar el mensaje en el intercambio 'alertas_seguridad'
    channel.basic_publish(exchange='alertas_seguridad', routing_key='', body=mensaje)
    
    print(f"[x] Alerta enviada: {mensaje}")
    
    # Cerrar la conexión
    connection.close()

# Ejemplo de mensaje de alerta
mensaje_alerta = {
    'fecha_hora': '2024-10-02T14:55:00',
    'ubicacion': 'Zona A - Estacionamiento',
    'descripcion': 'Se detectó comportamiento sospechoso cerca de un automóvil estacionado.'
}

# Publicar la alerta
publicar_alerta_seguridad(mensaje_alerta)