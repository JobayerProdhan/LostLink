from enum import Enum 
from fastapi import FastAPI 
from pydantic import BaseModel 

app = FastAPI() 
 
 
class ItemStatus(str,Enum):
    lost = "lost" 
    found = "found" 

class Item(BaseModel):
    name:str 
    category:str
    location:str
    date:str 
    description:str 
    status : ItemStatus 

items_db = [] 

# Request body --> create an item 
@app.post("/items/")
async def create_item(item:Item):
    items_db.append(item) 
    return item 


# Qurey Parameter --> Search/filter items 
@app.get("/items/") 
async def get_items(
    category:str | None =  None ,
    location:str | None = None,
    status:ItemStatus | None = None
):
    results = items_db 
    
    if  category:
        results = [item for item in results if item.category == category]
    
    if location:
        results = [item for item in results if item.location == location] 
    
    if status:
        results = [item for item in results if item.status == status] 
    
    return results

