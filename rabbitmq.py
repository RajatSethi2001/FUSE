from email.base64mime import header_length
import pika
import json

class mqMsgqIo(object):
  conn = None
  channel = None
  status = None
  qName = None
  def __init__(self, host='localhost'):
    self.conn = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1', heartbeat=100))
    self.channel = self.conn.channel()
  def msgqDeclare(self,qName,init=False):
    try:
      self.qName = qName
      if init:
        self.channel.queue_delete(queue=self.qName)
    except:
      pass
    self.channel.queue_declare(queue=self.qName)
  def push(self,data):
    self.channel.basic_publish(exchange='',routing_key=self.qName, body=data)
  def workerize(self,callback):
    self.channel.basic_consume(callback, queue=self.qName)#, no_ack=True)
    self.channel.start_consuming()
  def process_data_events(self):
    self.conn.process_data_events()

  def close(self):
    self.conn.close()

def wrap(data):
  try:
    wrapped_data = json.dumps(data)
  except:
    wrapped_data = None
  return wrapped_data

def unwrap(wrapped_data):
  try:
    data = json.loads(wrapped_data)
  except:
    data = None
  return data
