from fastapi import FastAPI
from typing import Union

app = FastAPI()
fake_item_db = {"dog":{"price":2.1, "num":10}, "cat":{"price":3.7, "num":20}}

@app.get("/items/{item_id}")
def read_item(item_id: str, q: Union[str, None] = None):
    if q:
        return fake_item_db[item_id][q]
    return fake_item_db[item_id]

