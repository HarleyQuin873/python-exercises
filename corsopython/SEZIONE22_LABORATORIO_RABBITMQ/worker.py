import pika

print("Collegamento a RabbitMQ...")

# params = pika.ConnectionParameters(host="localhost")
# connection = pika.BlockingConnection(params)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='worker_queue')

print("....eseguito")

# def callback(ch, method, properties, body):
#     print(" [x] Received %r" % body)


def callback(ch, method, properties, body):
    print("Ricevuto %s" % body)

# channel.basic_consume(callback, queue='worker_queue', no_ack=True)
# Correzione: passare gli argomenti come keyword arguments
channel.basic_consume(queue='worker_queue', on_message_callback=callback, auto_ack=True)

# channel.start_consuming()
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
