import pika # type: ignore

class Queue:
    def __init__(self, queue, connection=None, channel=None, prefetch_size=64, producer_fn=None, callback_fn=None, host='localhost', routing='route'):
        self.connection = connection if connection else pika.BlockingConnection(pika.ConnectionParameters(host=host))
        self.channel = self.connection.channel()
        self.routing = routing 
        self.queue = queue 
        self.callback_fn = callback_fn 
        self.producer_fn = producer_fn 
        self.prefetch_size = prefetch_size
    
    def send(self, body: bytes):
        self.channel.basic_publish(
            exchange='', 
            routing_key=self.queue,
            properties=pika.BasicProperties(content_type="application/json", delivery_mode=2),
            body=body
        )

    def consume(self):
        print(f"Waiting for messages in queue: {self.queue}. To exit press CTRL+C")
        self.channel.queue_declare(queue=self.queue, durable=True)
        self.channel.basic_consume(self.queue, self.callback_fn, False)
        self.channel.start_consuming()
