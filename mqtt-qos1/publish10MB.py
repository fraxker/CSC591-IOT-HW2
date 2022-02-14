"""
Send File Using MQTT
"""
import time
import paho.mqtt.client as paho
import hashlib
import numpy as np
broker="127.0.0.1"
port=1883
#filename="DSCI0027.jpg"
filename1="10MB" # 100B file to send



topic="my-mqtt-topic"
qos=1
data_block_size=2000
fo1=open(filename1,"rb")

fout=open("1out.txt","wb") #use a different filename
# for outfile as I'm rnning sender and receiver together

#define callback
def on_message(client, userdata, message):
   time.sleep(1)
   #print("received message =",str(message.payload.decode("utf-8")))
   fout.write(message.payload)

def on_publish(client, userdata, mid):
    #logging.debug("pub ack "+ str(mid))
    client.mid_value=mid
    client.puback_flag=True  

def c_publish(client,topic,out_message,qos):
   res,mid=client.publish(topic,out_message,qos)

client= paho.Client("client-001")  #create client object client1.on_publish = on_publish                          #assign function to callback client1.connect(broker,port)                                 #establish connection client1.publish("data/files","on")  
######
client.on_message=on_message
client.on_publish=on_publish
client.puback_flag=False #use flag in publish ack
client.mid_value=None
#####
throughput1=[]

print("connecting to broker ",broker)
client.connect(broker, port=port)#connect
client.loop_start() #start loop to process received messages
print("subscribing ")
client.subscribe(topic)#subscribe
count=0

while count<10:
   start=time.time()
   Run_flag=True
   while Run_flag:
      chunk=fo1.read(data_block_size) # change if want smaller or larger data blcoks
      if chunk:
         out_message=chunk
         #print(" length =",type(out_message))
         c_publish(client,topic,out_message,qos)
            
      else:
         res,mid=client.publish("my-mqtt-topic",out_message,qos=1)#publish
         Run_flag=False
   time_taken=time.time()-start
   throughput1.append(8000/time_taken) #Converting throughput in 10MB/sec to kilobits/second

   count=count+1



print("AVERAGE THROUGHPUT FOR 10MB FILE IS ",np.average(throughput1))
print("STANDARD DEVIATION IN THROUGHPUT FOR 10MB FILE IS ",np.std(throughput1))

client.disconnect() #disconnect
client.loop_stop() #stop loop
fout.close() #close files
fo1.close()