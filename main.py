from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel



app = FastAPI()

@app.get ("/")
async def root():
    return {"message":"hello world"}

@app.post("/")
async def post():
    return{"message":"hello pradeep"}

@app.get ("/",description="This is our first route")
async def base_get_route():
    return {"message":"helloo world"}

@app.get("/users")
async def list_users():
    return {"message":"list users route"}

@app.get ("/users/me")
async def get_current_user():
    return {"Message":"this is the current user"}

@app.get("/users/{user_id}")
async def get_users(user_id:str):
    return {"users_id":user_id}

class FoodEnum (str,Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"

@app.get ("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return{"food_name":food_name,"message":"you are healthy"}
    if food_name.value=="fruits":
        return{"food_name":food_name,"message":"you are still healthy"}
    return {"food_name":food_name,"message":"I like chocolate milk"}

fake_items_db=[{"items_name":"Foo"},{"item_name":"Bar"},{"item_name":"Baz"}]

@app.get("/items")
async def list_items (skip: int = 0, limit:int =10):
    return fake_items_db[skip:skip+limit]

@app.get ("/items/{item_id}")
async def get_item (item_id : str ,sample_query_param : str, q : str | None = None, short: bool = False ):
    item= {"item_id":item_id}
    if q:
        item.update({"q":q})
    if not short:
        item.update({"description":"Lorem"})
    return item

class Item(BaseModel):
    name : str
    description : str
    price : float
    tax : float | None= None

@app.post("/items")
async def create_new(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

@app.put("/items/{item_id}")
async def create_item_with_put(item_id: int, item:Item, q: str | None= None):
    result = {"item_id": item_id,**item.dict()}
    if q:
        result.update({"q":q})
    return result

    #     return{"item_id":item_id,"q":q}
    # return {"item_id":item_id}
