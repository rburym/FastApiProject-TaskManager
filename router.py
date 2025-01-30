from typing import Annotated
from fastapi import APIRouter, Depends
from repository import TaskRepository
from models import STaskAdd, STask, STaskId

router = APIRouter(
    prefix="/tasks",
    tags=["Таски"],
)

@router.post("")
async def add_tasks(
    task: Annotated[STaskAdd, Depends(), ],
) -> STaskId:
    """
    Создает новую таску

    :param task: Описание таски. Ожидается объект типа STaskAdd
    :return: Возвращает объект типа STaskId, Id таски и статус
    """
    await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task.id}


@router.get("")
async def get_tasks() -> list[STask]:
    """
    Возвращает список всех задач

    :return: объект типа STask
    """
    tasks = await TaskRepository.find_all()
    return tasks

