from fastapi import FastAPI
from src.api.grand_exchange.grand_exchange import GrandExchangeApi

app = FastAPI()
ge_api = GrandExchangeApi()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/grand_exchange/selected_items")
async def get_selected_items():
    items = ge_api.map_selected_items()
    return {"selected_items": items}