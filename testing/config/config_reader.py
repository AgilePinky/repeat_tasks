import json

class ConfigReader:

    CONFIG_PATH = "config/config.json"

    def __init__(self, config_path=CONFIG_PATH):
        with open(config_path) as config_file:
            self.config = json.load(config_file)

    def get_base_url(self):
        return self.config["base_url"]

    def get_timeout(self):
        return self.config["timeout"]