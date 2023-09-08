from pydantic import BaseModel

class Todo(BaseModel):
    name: str
    price: float
    id: int