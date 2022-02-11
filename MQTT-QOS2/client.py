# from statistics import mean, stdev
# from unittest import result
# import requests
# from pathlib import Path
# import time

# DATAFILES = Path("/DataFiles")

# HundredB = DATAFILES.joinpath("100B")
# TenKB = DATAFILES.joinpath("10KB")
# OneMB = DATAFILES.joinpath("1MB")
# TenMB = DATAFILES.joinpath("10MB")

# def downlink(file: Path, repeat: int, size: int):
#     times = []
#     sizes = []
#     with file.open("rb") as f:
#         for _ in range(repeat):
#             start_time = time.time()
#             r = requests.post("http://server:5000", files={"upload_file": f})
#             sizes.append(r.json()["size"])
#             times.append(time.time() - start_time)
    
#         print(file.name, "Throughput Mean in kilobits:", size * 0.008 / mean(times))
#         print(file.name, "Throughput STD in kilobits:", size * 0.008 / stdev(times))
#         print(file.name, "Packet Size Mean in kilobits:", mean(sizes) * 0.008)

# if __name__ == "__main__":
#     # Downlink 100 B file
#     print("Downlinking 100B file")
#     downlink(HundredB, 10000, 100)

#     # Downlink 10kB file
#     print("Downlinking 10KB file")
#     downlink(TenKB, 1000, 10000)

#     # Downlink 1MB file
#     print("Downlinking 1MB file")
#     downlink(OneMB, 100, 1000000)

#     # Downlink 10MB file
#     print("Downlinking 10MB file")
#     downlink(TenMB, 10, 10000000)

    ######
#simulator device 1 for mqtt message publishing
import paho.mqtt.client as paho
import time
import random
#hostname
broker="mosquitto"
#port
port=1883
def on_publish(client,userdata,result):
    print("Device 1 : Data published.")
    pass
client= paho.Client("admin")
client.on_publish = on_publish
client.connect(broker,port)
for i in range(20):
    d=random.randint(1,5)
    
 #telemetry to send 
message="Device 1 : Data " + str(i)
time.sleep(d)
    
 #publish message
ret= client.publish("/data",message)
print("Stopped...")