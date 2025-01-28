from asyncio import tasks
from contextlib import asynccontextmanager
from typing import Optional, Annotated
from fastapi import FastAPI, Depends
from pydantic import BaseModel

#импортируем все модели

from contextlib import asynccontextmanager
#позволяет создавать контекст менеджер

from sqlalchemy.testing.util import drop_all_tables

from models import create_tables, delete_tables




@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Жизненный цикл
    :param app:
    :return:
    """
    await delete_tables()
    print("База очищена")
    await create_tables()
    print("База готова к работе")
    yield
    print("Выключение")

app = FastAPI(lifespan=lifespan)

class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None

class STask(STaskAdd):
    id: int



tasks = []

@app.get("/tasks")
async def add_tasks(
    task: Annotated[STaskAdd, Depends(), ],
):
    tasks.append(task)
    return {"ok": True}


# @app.get("/tasks")
# def get_tasks():
#     task = Task(name="Сделай тест")
#     return {"data": task}
#
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}
#
#
# @app.get("/home")
# def get_home():
#     return "Hello World!"