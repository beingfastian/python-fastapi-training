from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Item(BaseModel):
    id: Optional[int] = None  
    name: str
    description: Optional[str] = None
    is_active: bool = True

items: List[Item] = []
next_id = 1  
@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    global next_id
    item.id = next_id
    next_id += 1
    items.append(item)
    return item

@app.get("/items/", response_model=List[Item])
async def get_items():
    return items

# 🔵 READ - Get a specific item by ID
@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, updated_item: Item):
    for index, existing_item in enumerate(items):
        if existing_item.id == item_id:
            updated_item.id = item_id  # Keep the same ID
            items[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item.id == item_id:
            del items[index]
            return {"message": f"Item with ID {item_id} deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")
