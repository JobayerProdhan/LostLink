from enum import Enum 
from fastapi import FastAPI ,HTTPException  
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

# path parameter --> get specific  item 
@app.get("/itms/{items_id}")
async def get_items(items_id:int):
    if items_id >= len(items_db):
        raise HTTPException (status_code=404,detail="Items not found") 



# put --> Replace the entire item  
@app.put("/items/{items_id}") 
async def update(item_id:int , item:Item):
    if item_id>=len(items_db):
        raise HTTPException(status_code=404,detail='Items not  found') 
    
    items_db[item_id] = item
    return items_db[item_id] 