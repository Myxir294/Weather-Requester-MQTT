from datetime import datetime
import requests
import json

class Weather_Requestor:
    def __init__(self, location): 
        self.set_location = location
        self.url = "https://api.openaq.org/v2/latest/" + str(self.set_location) + "?limit=100&page=1&offset=0&sort=asc"
        self.headers = {"accept": "application/json"}
        self.time = datetime.now().isoformat()
        self.dictionary = {}
        self.json_processed_data = ""

    def download_data(self):
        self.response = requests.get(self.url, headers=self.headers)
        self.raw_json_text = json.loads(self.response.text)
        self.time = datetime.now().isoformat();
        self.dictionary = {}
        self.dictionary.update({"location" : self.raw_json_text ["results"][0]["location"]})
        self.dictionary.update({"timestamp" : str(self.time)})

        values_dictionary = {}
        for element in self.raw_json_text["results"][0]["measurements"]:
            values_dictionary.update({element["parameter"] : element["value"]})
        self.dictionary.update({"values" : values_dictionary})

        self.json_processed_data = json.dumps(self.dictionary, skipkeys = True, allow_nan = True, ensure_ascii=False)
        #print(self.json_processed_data)
        #print(" ")

