"""
Send File Using MQTT
"""
import time
import paho.mqtt.client as paho
import hashlib
import numpy as np

broker="mosquitto"
port=1883



#define callback
def on_message(client, userdata, message):
   time.sleep(1)
   fout.write(message.payload)
   #print("received message =",str(message.payload.decode("utf-8")))

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

topic="my-mqtt-topic"
print("connecting to broker ",broker)
client.connect(broker, port=port)#connect
client.loop_start() #start loop to process received messages
print("subscribing ")
client.subscribe(topic)#subscribe

fout=open("publishLog.txt","wb")

filename1= "100B" # 100B file to send
qos=2
data_block_size=2000
fo1=open(filename1,"rb")
throughput1=[]
count=0
while count<10000:
   start=time.time()
   Run_flag=True
   while Run_flag:
      chunk=fo1.read(data_block_size) # change if want smaller or larger data blcoks
      if chunk:
         out_message=chunk
         #print(" length =",type(out_message))
         c_publish(client,topic,out_message,qos)
            
      else:
         res,mid=client.publish("my-mqtt-topic",out_message,qos=2)#publish
         Run_flag=False
   time_taken=time.time()-start
   throughput1.append(0.8/time_taken) #converting throughput in 100bytes/second to kilobits/second

   count=count+1
fo1.close()

print("AVERAGE THROUGHPUT FOR 100B FILE IS ",np.average(throughput1))
print("STANDARD DEVIATION IN THROUGHPUT FOR 100B FILE IS ",np.std(throughput1))

filename1="10KB" # 10KB file to send
qos=2
data_block_size=2000
fo1=open(filename1,"rb")
throughput1=[]
count=0
while count<10000:
   start=time.time()
   Run_flag=True
   while Run_flag:
      chunk=fo1.read(data_block_size) # change if want smaller or larger data blcoks
      if chunk:
         out_message=chunk
         #print(" length =",type(out_message))
         c_publish(client,topic,out_message,qos)
            
      else:
         res,mid=client.publish("my-mqtt-topic",out_message,qos=2)#publish
         Run_flag=False
   time_taken=time.time()-start
   throughput1.append(8/time_taken) #converting throughput in 10kilobytes/second to kilobits/second

   count=count+1
fo1.close()

print("AVERAGE THROUGHPUT FOR 10KB FILE IS ",np.average(throughput1))
print("STANDARD DEVIATION IN THROUGHPUT FOR 10KB FILE IS ",np.std(throughput1))


filename1="1MB" # 1MB file to send
qos=2
data_block_size=2000
fo1=open(filename1,"rb")
throughput1=[]
count=0
while count<10000:
   start=time.time()
   Run_flag=True
   while Run_flag:
      chunk=fo1.read(data_block_size) # change if want smaller or larger data blcoks
      if chunk:
         out_message=chunk
         #print(" length =",type(out_message))
         c_publish(client,topic,out_message,qos)
            
      else:
         res,mid=client.publish("my-mqtt-topic",out_message,qos=2)#publish
         Run_flag=False
   time_taken=time.time()-start
   throughput1.append(8000/time_taken) #converting throughput in 1megabyte/second to kilobits/second

   count=count+1
fo1.close()

print("AVERAGE THROUGHPUT FOR 1MB FILE IS ",np.average(throughput1))
print("STANDARD DEVIATION IN THROUGHPUT FOR 1MB FILE IS ",np.std(throughput1))

filename1="10MB" # 100B file to send
qos=2
data_block_size=2000
fo1=open(filename1,"rb")
throughput1=[]
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
         res,mid=client.publish("my-mqtt-topic",out_message,qos=2)#publish
         Run_flag=False
   time_taken=time.time()-start
   throughput1.append(80000/time_taken) #Converting throughput in 10MB/sec to kilobits/second

   count=count+1
fo1.close()

print("AVERAGE THROUGHPUT FOR 10MB FILE IS ",np.average(throughput1))
print("STANDARD DEVIATION IN THROUGHPUT FOR 10MB FILE IS ",np.std(throughput1))


client.disconnect() #disconnect
client.loop_stop() #stop loop
fout.close()
