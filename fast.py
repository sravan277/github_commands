from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pydantic_core.core_schema import model_field


app = FastAPI()

items = {}


class Item(BaseModel):
    item: str = None
    token :int = 0;


@app.get("/")
def root():
    return {"Message":"Hello world"}



@app.get("/{id}", response_model=Item)
def getitem(id: int):
    if id not in items:
        raise HTTPException(status_code=404, detail=f"The item{id} is not found")
    return Item(item = items[id], token=id)


@app.post("/")
def addItem(data: Item):
    items[data.token] = data.item;
    return items