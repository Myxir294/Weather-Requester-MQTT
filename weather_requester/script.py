import os
import time

from data_requestor import Weather_Requestor
from MQTT_communication import MQTT_communication_class


os.environ["LOCATION"] = "10566"

my_data_requestor = Weather_Requestor(os.environ['LOCATION'])

mqtt_communication = MQTT_communication_class("252964", "46.101.199.108", 1883, "sys-wbud", "student")

#basepath = os.path.dirname(__file__)
#file = open(("topics/test"), "w")

while 1:
    
    #print("Below data read from weather sensors web service")
    my_data_requestor.download_data()
    time.sleep(5)

    print("Received data send over MQTT with below topic")
    mqtt_communication.mqtt_publish_data(my_data_requestor.json_processed_data, my_data_requestor.raw_json_text)
    time.sleep(5)

    print("Proceed to subscribe from MQTT server")
    mqtt_communication.mqtt_receive_data_from_all_topics();
    time.sleep(5)
