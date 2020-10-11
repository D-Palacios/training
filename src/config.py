import json
import os

CONFIG_FILENAME = "/root/src/config/" + os.getenv("CONFIG_FILE","configuration.json")

class Configuration:
    
    def __init__(self):
        self.data = self._load_config()


    def _load_config(self):
        with open(CONFIG_FILENAME) as json_file:
            return json.load(json_file)