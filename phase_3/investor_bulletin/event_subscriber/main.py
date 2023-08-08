from pika import BlockingConnection, ConnectionParameters
# Create a connection object to start consuming events

def init_subscriber():

  connection =  BlockingConnection(ConnectionParameters(host="localhost", port=5672))
  channel = connection.channel()
  channel.queue_declare(queue="THRESHOLD_ALERTS_QUEUE")
  return channel

def on_event(ch, method, properties, body):
  print(f"Alert received: {body}")

if __name__ == "__main__":
    import os, sys
    current_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(current_dir)
    sys.path.append(root_dir)

    subscriber = init_subscriber()
    subscriber.basic_consume(queue="THRESHOLD_ALERTS_QUEUE", on_message_callback=on_event, auto_ack=True)
    subscriber.start_consuming()
    subscriber.close()
