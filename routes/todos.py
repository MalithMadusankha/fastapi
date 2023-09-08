from fastapi import APIRouter
from models.todos import Todo

todos = APIRouter()

todos_list = []

@todos.get("/todos")
async def get_todos():
    return {"todos": todos_list}

@todos.post("/todos")
async def create_todos(todo: Todo):
    todos_list.append(todo)
    return {"todo": todo}
