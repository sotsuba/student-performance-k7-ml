from core.queue import Queue
import pika 
from time import sleep 

def connect_to_rabbitmq(server):
    for _ in range(10):
        try:
            crd = pika.credentials.PlainCredentials('guest', 'guest') # Create credentials object with username and password like in docker-compose.yml
            port = 5672 # Default port for RabbitMQ
            connection = pika.BlockingConnection(pika.ConnectionParameters(host=server, port=port, credentials=crd))
            channel    = connection.channel()
            print("SUCCESS: instantiated RabbitMQ connection and channel")
            return connection, channel
        except Exception as e:
            print(
                f"Trying to instantiate connection and channel with RabbitMQ server {server} with error {e}"
            )
            sleep(10)
            pass

def teardown_queue(queue_name, server="localhost"):
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=server))
        channel = connection.channel()
        channel.queue_delete(queue=queue_name)
        print(f"Queue {queue_name} deleted")
    except Exception as e:
        print(str(e))