from typing import List, Optional
from pydantic import BaseModel

class ItemData(BaseModel):
    id: int
    name: str
    examine: str
    members: bool

    limit: Optional[int] = None
    lowalch: Optional[int] = None
    highalch: Optional[int] = None
    value: int

class MappingResponseData(BaseModel):
    itemsData: List[ItemData]

class ItemPriceData(BaseModel):
    high: int | None = None
    highTime: int | None = None
    low: int | None = None
    lowTime: int | None = None

class LatestResponseData(BaseModel):
    data: dict[str, ItemPriceData]
    