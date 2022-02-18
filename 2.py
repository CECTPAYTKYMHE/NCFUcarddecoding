import pika
import time
import pika, sys, os
import json
def main():
    credential = pika.PlainCredentials('a_ivanov', 'bU=Ub53f$4')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='10.200.64.192',credentials=credential))
    channel = connection.channel()
    channel.queue_declare(queue='sys.queues.ad_debug',durable=True)
    channel.basic_qos
    def callback(ch, method, properties, body):
        msg = json.loads(body)
        print(" [x] Received %r" % msg)
        time.sleep(1)
        return msg
        
            
    
    channel.basic_consume(queue='sys.queues.ad_debug', on_message_callback=callback, auto_ack=False)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    
    channel.start_consuming()
    channel.stop_consuming()
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

