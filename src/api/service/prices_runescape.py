from src.api.model.prices_runescape import MappingResponseData, LatestResponseData

import requests
import os
from dotenv import load_dotenv

load_dotenv()

class GrandExchangeApi:
    BASE_URL: str = os.getenv('GE_BASE_URL')

    def __init__(self):
        self.headers = {
            'User-Agent': os.getenv('USER_AGENT')
        }
        

    def get_mapping(self) -> MappingResponseData | None:
        URL = GrandExchangeApi.BASE_URL + "mapping"
        print(f"=> Consulta de mapping. Url: '{URL}'")

        response = requests.get(URL, headers=self.headers)
        print(f'Status: {str(response.status_code)}')
        if response.status_code == 200:
            data = response.json()
            mapping_response = MappingResponseData(itemsData=data)
            return mapping_response

    def get_latest(self) -> LatestResponseData | None:
        URL = GrandExchangeApi.BASE_URL + "latest"
        print(f"=> Consulta de latest. Url: '{URL}'")

        response = requests.get(URL, headers=self.headers)
        print(f'Status: {str(response.status_code)}')
        if response.status_code == 200:
            data = response.json()
            latestResponseData = LatestResponseData(**data)
            return latestResponseData
