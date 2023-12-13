import time
import requests
import os
import json

os.environ["LOCATION"] = "333"

class Weather_Requestor:
    def __init__(self, location):
        self.set_location = location
        self.url = "https://api.openaq.org/v2/latest/" + str(self.set_location) + "?limit=100&page=1&offset=0&sort=asc"
        self.headers = {"accept": "application/json"}
        self.time = time.ctime()

    def output(self):
        self.response = requests.get(self.url, headers=self.headers)
        self.temp = json.loads(self.response.text)
        self.time = time.ctime()
        print("{\"location\": <" , self.temp["results"][0]["location"] + ">,")
        print(" \"timestamp\": <" + str(self.time) + ">,")
        print("\"values\":[")
        print("{ " + self.temp["results"][0]["measurements"][0]["parameter"] + " : " + str(self.temp["results"][0]["measurements"][0]["value"]) + " " + self.temp["results"][0]["measurements"][0]["unit"] ) 
        print("  " + self.temp["results"][0]["measurements"][1]["parameter"] + " : " + str(self.temp["results"][0]["measurements"][1]["value"]) + " " + self.temp["results"][0]["measurements"][1]["unit"] )
        print("]}")
        print(" ")
        print(" ")

myrequestor = Weather_Requestor(os.environ['LOCATION'])

while 1:

    myrequestor.output()
    time.sleep(30)


