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

    def output(self):
        self.response = requests.get(self.url, headers=self.headers)
        self.temp = json.loads(self.response.text)
        #print(self.temp["results"])
        print(self.temp["results"][0])
        #print(self.temp["results"][0]["location"])
        #for element in self.temp["results"]:
        #    print (element)

myrequestor = Weather_Requestor(os.environ['LOCATION'])

while 1:

    time.sleep(3)
    myrequestor.output()


