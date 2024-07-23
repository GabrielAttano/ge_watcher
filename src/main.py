from fastapi import FastAPI

from src.api.service.ge_watcher import GeWatcher

ge_watcher = GeWatcher()
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/grand_exchange/selected_items")
async def get_selected_items():
    items = ge_watcher.get_selected_items()
    return items