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

class MappingResponse(BaseModel):
    itemsData: List[ItemData]

class ItemPriceData(BaseModel):
    high: int | None = None
    highTime: int | None = None
    low: int | None = None
    lowTime: int | None = None

class LatestResponse(BaseModel):
    data: dict[str, ItemPriceData]

class itemTimeseriesData(BaseModel):
    timestamp: int
    avgHighPrice: int | None = None
    avgLowPrice: int | None = None
    highPriceVolume: int
    lowPriceVolume: int

class TimeSeriesResponse(BaseModel):
    data: List[itemTimeseriesData]
    itemId: int
    