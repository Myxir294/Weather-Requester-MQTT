from datetime import datetime
import requests
import os
import json
import time

#os.environ["LOCATION"] = "323"

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

        json_string = json.dumps(self.dictionary, skipkeys = True, allow_nan = True)
        print(json_string)
        print(" ")

myrequestor = Weather_Requestor(os.environ['LOCATION'])

while 1:

    myrequestor.output()
    time.sleep(10)


