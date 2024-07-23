from src.api.model.prices_runescape import MappingResponse, LatestResponse, TimeSeriesResponse

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
        

    def get_mapping(self) -> MappingResponse | None:
        URL = GrandExchangeApi.BASE_URL + "mapping"
        print(f"=> Consulta de mapping. Url: '{URL}'")

        response = requests.get(URL, headers=self.headers)
        print(f'Status: {str(response.status_code)}')
        if response.status_code == 200:
            data = response.json()
            mapping_response = MappingResponse(itemsData=data)
            return mapping_response

    def get_latest(self) -> LatestResponse | None:
        URL = GrandExchangeApi.BASE_URL + "latest"
        print(f"=> Consulta de latest. Url: '{URL}'")

        response = requests.get(URL, headers=self.headers)
        print(f'Status: {str(response.status_code)}')
        if response.status_code == 200:
            data = response.json()
            latest_response = LatestResponse(**data)
            return latest_response

    def get_timeseries(self, id: str) -> TimeSeriesResponse | None:
        URL = GrandExchangeApi.BASE_URL + "timeseries"
        params = {
            "timestep": "5m",
            "id": id
        }
        print(f"=> Consulta de timeseries. Url: '{URL}' | params: '{params}'")

        response = requests.get(URL, headers=self.headers, params=params)
        if response.status_code == 200:
            data = response.json()
            timeseries_response = TimeSeriesResponse(data=data["data"], itemId=data["itemId"])
            return timeseries_response

if __name__ == "__main__":
    ge_api = GrandExchangeApi()
    timeseries_response = ge_api.get_timeseries("1127")
    print(timeseries_response.data[0])