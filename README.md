# Sistema de Publicador-Suscriptor para Alertas de Seguridad

Este proyecto implementa un sistema de **Publicador-Suscriptor** utilizando [RabbitMQ](https://www.rabbitmq.com/), un intermediario de mensajes que permite gestionar las comunicaciones asíncronas entre aplicaciones.

## Descripción

El sistema se encarga de enviar (publicador) y recibir (suscriptor) mensajes de alerta de seguridad a través de un patrón de intercambio (`exchange`) de tipo `fanout`. Las alertas se envían en formato JSON y contienen información sobre el tipo de alerta, la ubicación y una descripción detallada.

## Características

- **Publicador-Suscriptor**: El sistema sigue un modelo en el cual un "Publicador" envía alertas de seguridad y múltiples "Suscriptores" pueden recibirlas y procesarlas.
- **RabbitMQ**: Utiliza RabbitMQ para gestionar la cola de mensajes.
- **Mensajes JSON**: Las alertas se envían y reciben en formato JSON, facilitando la interpretación y manejo de datos.

## Configuración e Instalación

### Requisitos

- [Python 3.x](https://www.python.org/)
- [RabbitMQ](https://www.rabbitmq.com/) instalado y ejecutándose localmente.
- Biblioteca `pika` para la comunicación con RabbitMQ:

```bash
pip install pika
