import paho.mqtt.client as mqtt
from paho.mqtt.properties import Properties
from paho.mqtt.packettypes import PacketTypes 

def on_message(client, userdata, message, properties=None):
        print(" Received message " + str(message.payload)
            + " on topic '" + message.topic
            + "' with QoS " + str(message.qos))
        processed_topic = message.topic.replace("/", "-")
        file = open ("/workspaces/vscode-remote-try-python/weather_requester/topics/" + (str(processed_topic)), "w")
        file.write(str(message.payload)) 

class MQTT_communication_class:
    def __init__(self, client_id, ip, port, password, user):

        self.client = mqtt.Client(client_id, transport='tcp', protocol=mqtt.MQTTv5)
        self.client.username_pw_set(user, password)
        self.client.on_message = on_message
        properties=Properties(PacketTypes.CONNECT)
        properties.SessionExpiryInterval=30*60 #seconds
        self.client.connect(ip, port, clean_start=mqtt.MQTT_CLEAN_START_FIRST_ONLY, properties=properties, keepalive=60)
        self.client.loop_start()

    def mqtt_publish_data(self, json_string, topic_data):

        self.topic = str(self.client._client_id)[1:-1] + '/' + str(topic_data["results"][0]["location"])  #'topic/important'
        #self.topic = (unicodedata.normalize('NFD', self.topic).encode('ascii', 'ignore')).decode('ascii', 'ignore')
        self.topic = self.topic.encode('ascii', 'ignore').decode('ascii', 'ignore')[1:]
        print(self.topic)
        
        #print("After subscribe")
        #self.client.subscribe(self.topic,2)
        properties=Properties(PacketTypes.PUBLISH)
        properties.MessageExpiryInterval=30 # in seconds
        self.client.publish(self.topic,json_string,2,properties=properties,retain=True);

        #self.client.subscribe()

    def mqtt_receive_data_from_all_topics(self):
         
        self.client.subscribe("#",2)
