# from flask import Flask, request
# app = Flask(__name__)

# @app.route('/', methods=['POST'])
# def hello_world():
#     return {"size": request.content_length}

######
import paho.mqtt.client as mqtt
# This is the Subscriber
#hostname
broker="mosquitto"
#port
port=1883
#time to live
timelive=60
def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("/data")
def on_message(client, userdata, msg):
    print(msg.payload.decode())
    
client = mqtt.Client()
client.connect(broker,port,timelive)
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()
