from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI(title="Flask‑Todo‑API", version="1.0.0")

class TodoItem(BaseModel):
    id: int = Field(..., example=1)
    title: str = Field(..., min_length=1, example="Buy milk")
    completed: bool = Field(default=False, example=False)

# In‑memory store (for demo purposes)
_ITEMS: List[TodoItem] = []

@app.get("/todos", response_model=List[TodoItem])
def list_todos():
    return _ITEMS

@app.post("/todos", response_model=TodoItem, status_code=201)
def create_todo(item: TodoItem):
    if any(existing.id == item.id for existing in _ITEMS):
        raise HTTPException(status_code=400, detail="Todo with this ID already exists")
    _ITEMS.append(item)
    return item

@app.get("/todos/{todo_id}", response_model=TodoItem)
def get_todo(todo_id: int):
    for item in _ITEMS:
        if item.id == todo_id:
            return item
    raise HTTPException(status_code=404, detail="Todo not found")

@app.put("/todos/{todo_id}", response_model=TodoItem)
def update_todo(todo_id: int, updated: TodoItem):
    for idx, item in enumerate(_ITEMS):
        if item.id == todo_id:
            _ITEMS[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int):
    global _ITEMS
    _ITEMS = [item for item in _ITEMS if item.id != todo_id]
    return
