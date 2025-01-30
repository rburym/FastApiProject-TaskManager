from models import new_session, TaskOrm, STaskAdd, STask
from sqlalchemy import select


class TaskRepository:
    @classmethod
    async def add_task(cls, data: STaskAdd) -> int:
        """
        Добавляет новую задачу в бд.

        :param data: Данные задачи, ожидается объект типа STaskAdd
        :return: Ид задачи (int)
        """
        async with new_session() as session:
            task_dict = data.model_dump()
            task = TaskOrm(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id


    @classmethod
    async def find_all(cls) -> list[STask]:
        """
        Возвращает список всех задач из бд.

        :return: Список задач, представлен объектом типа STask.
        """
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalats().all()
            task_schemas = [STask.model_validate(task) for task in task_models]
            return task_models