# No.3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
  name: str
  price: float


items_db = {
  1: {"name": "Item 1", "price": 214.6},
  2: {"name": "Item 2", "price": 300.2},
}

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
  if item.price < 0:
    raise HTTPException(status_code=400, detail="Price cannot be negative")
  
  items_db[len(items_db) + 1] = {"name": item.name, "price": item.price}
  return item

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
  item = get_item_by_id(item_id)
  if item is None:
    raise HTTPException(status_code=404, detail="Item not found")
  return item

def get_item_by_id(item_id: int) -> Optional[Item]:
  item_data = items_db.get(item_id)
  if item_data:
    return Item(**item_data)
  return None


# Changes made :-

# In-memory storage: We introduce the "items_db" dictionary to store items to simulate a database for demonstration purpose.

# End point "create_item": We create a new "item_id" using `items_db` plus the length. We store items in "items_db" with generated `item_id`.

# Destination "read_object": We can retrieve items by ID by calling "get_item_by_id".

# Function "get_item_by_id": This function retrieves items from "items_db" using the provided "item_id". If there is no such item, "None" is returned.