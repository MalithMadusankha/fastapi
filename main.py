from fastapi import FastAPI
from pydantic import BaseModel
from routes.todos import todos

app = FastAPI()

todoList = []

class Item(BaseModel):
    name: str
    price: float
    id: int

print("<======== Server Started =======>")\
    
app.include_router(todos)
