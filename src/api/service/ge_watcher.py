from src.api.service.prices_runescape import GrandExchangeApi
from src.api.model.ge_watcher import Item, SelectedItemsResponse

class GeWatcher():
    def __init__(self) -> None:
        self.ge_api = GrandExchangeApi()

    def get_selected_items(self) -> SelectedItemsResponse | None:
        latest_response = self.ge_api.get_latest()
        mapping_response = self.ge_api.get_mapping()
        if latest_response == None or mapping_response == None:
            return 
        
        items_id = ["1319", "1359", "1373", "4131", "1113", "9185", "1163", "1303", "1147", "1275", "1127", "1079", "1093", "1333", "1185", "1289"]
        
        selected_items = []
        for item_data in mapping_response.itemsData:
            id = str(item_data.id)
            if id in items_id:
                item_price_data = latest_response.data[id]
                print(item_data)
                print(item_price_data)
                item = Item(priceData=item_price_data, itemData=item_data)
                selected_items.append(item)
        
        selected_items_response = SelectedItemsResponse(selectedItems=selected_items)
        print(selected_items_response)
        return selected_items_response