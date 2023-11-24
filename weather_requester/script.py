import time
import requests
import os
print ("test")

#res = requests.get("https://api.openaq.org/v2/locations/2178", headers={"X-API-Key": "my-openaq-api-key-12345-6789"})

licznik = 0
location_name = "temp"
iso_current_time = "temp"
measurement_name = "temp"
value = "temp"

class Weather_Requestor:
    def __init__(self, location):
        self.set_location = location
        self.iso_current_time = "temp"
        self.measurement_name = "temp"
        self.value = "temp"

    def output(self):
        print (self.set_location + '\n' + "timestamp: " + self.iso_current_time + '\n' + "values: " + self.measurement_name + " " + value)

myrequestor = Weather_Requestor("test")

while licznik < 10:
    
    time.sleep(3)
    myrequestor.output()
    licznik = licznik + 3
