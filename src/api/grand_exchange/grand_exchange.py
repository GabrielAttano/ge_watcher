from src.api.ge_watcher.ge_watcher import GeWatcher

import requests
import os
from dotenv import load_dotenv

load_dotenv()

class Item:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.examine = ""
        self.members = False

        self.limit = 0
        self.low_alch = 0
        self.high_alch = 0
        self.value = 0

        self.high = 0
        self.high_time = "0"
        self.low = 0
        self.low_time = ""

    def set_mapping_attributes(self, mapping: dict):
        self.id = mapping["id"]
        self.name = mapping["name"]
        self.examine = mapping["examine"]
        self.members = mapping["members"]

        self.limit = mapping["limit"]
        self.low_alch = mapping["lowalch"]
        self.high_alch = mapping["highalch"]
        self.value = mapping["value"]

    def set_latest_attributes(self, latest: dict):
        self.high = latest["high"]
        self.low = latest["low"]
        self.high_time = latest["highTime"]
        self.low_time = latest["lowTime"]

    def __str__(self):
        return (f"Item(id={self.id}, name={self.name}, examine={self.examine}, "
                f"members={self.members}, limit={self.limit}, low_alch={self.low_alch}, "
                f"high_alch={self.high_alch}, value={self.value}, high={self.high}, "
                f"high_time={self.high_time}, low={self.low}, low_time={self.low_time})")

class GrandExchangeApi:
    BASE_URL: str = os.getenv('GE_BASE_URL')

    def __init__(self):
        self.headers = {
            'User-Agent': os.getenv('USER_AGENT')
        }
        self.ge_watcher = GeWatcher()
        

    def get_mapping(self) -> dict | None:
        URL = GrandExchangeApi.BASE_URL + "mapping"
        print(f"=> Consulta de mapping. Url: '{URL}'")

        response = requests.get(URL, headers=self.headers)
        print(f'Status: {str(response.status_code)}')
        if response.status_code == 200:
            return response.json()

    def get_latest(self) -> dict | None:
        URL = GrandExchangeApi.BASE_URL + "latest"
        print(f"=> Consulta de latest. Url: '{URL}'")

        response = requests.get(URL, headers=self.headers)
        print(f'Status: {str(response.status_code)}')
        if response.status_code == 200:
            return response.json()
        
    def map_selected_items(self, latest: dict) -> list:
        print("=> Mapeando itens selecionados.")
        
        selected_items = self.ge_watcher.get_items_to_watch()
        if selected_items == None:
            print("Erro ao consultar itens selecionados.")
            return
        
        mapping = self.get_mapping()
        if mapping == None:
            print("Erro na consulta de mapping dos itens.")
            return
        
        items = list()
        for map in mapping:
            id = str(map["id"])
            if id in selected_items:
                item = Item()
                item.set_mapping_attributes(map)
                latestAux = latest["data"][id]
                item.set_latest_attributes(latestAux)
                items.append(item)
        return items
            
geApi = GrandExchangeApi()
latest = geApi.get_latest()
items = geApi.map_selected_items(latest)
item: Item = items[0]
print(item)
