from typing import List
from pydantic import BaseModel
from src.api.model.prices_runescape import ItemData, ItemPriceData

class Item(BaseModel):
    priceData: ItemPriceData
    itemData: ItemData

class SelectedItemsResponse(BaseModel):
    selectedItems: List[Item] | None = None