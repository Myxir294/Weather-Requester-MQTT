from datetime import datetime
import requests
import os
import json
import time

import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
from paho.mqtt.properties import Properties
from paho.mqtt.packettypes import PacketTypes 
import ssl

client = mqtt.Client(client_id="student252964", transport='tcp', protocol=mqtt.MQTTv5)
client.username_pw_set("student", "sys_wbud")
client.tls_set(certfile=None,
               keyfile=None,
               cert_reqs=ssl.CERT_REQUIRED)

def on_message(client, userdata, message, properties=None):
   print(" Received message " + str(message.payload)
        + " on topic '" + message.topic
        + "' with QoS " + str(message.qos))

client.on_connect = on_message
   
properties=Properties(PacketTypes.CONNECT)
properties.SessionExpiryInterval=30*60 #sekundy

client.connect("46.101.108.102", 1883, clean_start=mqtt.MQTT_CLEAN_START_FIRST_ONLY, properties=properties, keepalive=60)

client.loop_start()

################lab 2

os.environ["LOCATION"] = "10566"

class Weather_Requestor:
    def __init__(self, location): 
        self.set_location = location
        self.url = "https://api.openaq.org/v2/latest/" + str(self.set_location) + "?limit=100&page=1&offset=0&sort=asc"
        self.headers = {"accept": "application/json"}
        self.time = datetime.now().isoformat()
        self.dictionary = {}

    def output(self):
        self.response = requests.get(self.url, headers=self.headers)
        self.temp = json.loads(self.response.text)
        self.time = datetime.now().isoformat();
        self.dictionary = {}
        self.dictionary.update({"location" : self.temp["results"][0]["location"]})
        self.dictionary.update({"timestamp" : str(self.time)})

        values_dictionary = {}
        for element in self.temp["results"][0]["measurements"]:
            values_dictionary.update({element["parameter"] : element["value"]})
        self.dictionary.update({"values" : values_dictionary})

        json_string = json.dumps(self.dictionary, skipkeys = True, allow_nan = True, ensure_ascii=False)
        print(json_string)
        print(" ")

myrequestor = Weather_Requestor(os.environ['LOCATION'])

while 1:

    myrequestor.output()
    time.sleep(10)

