
# from flask import Flask, request
# app = Flask(__name__)

# @app.route('/', methods=['POST'])
# def hello_world():
#     return {"size": request.content_length}

######
import paho.mqtt.client as mqtt
import sys
import time
# This is the Subscriber
#hostname
broker="mosquitto"
#port
port=1883
#time to live
timelive=60
def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc), flush=True)
  client.subscribe("/data", 2)
msg_array = []
msg_sig = False
def on_message(client, userdata, msg):
  print("received", flush=True)
  time.sleep(0.1)
  if(msg_sig == True and str(msg.payload) != "STOP"):
    msg_array.append(sys.getsizeof(msg))
  if(str(msg.payload)=="START"):
    print("START", flush=True)
    msg_sig = True
  if(str(msg.payload)=="STOP"):
    print("STOP", flush=True)
    msg_sig = False

client = mqtt.Client()
client.connect(broker,port,timelive)
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()
