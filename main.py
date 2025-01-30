from fastapi import FastAPI
from models import create_tables, delete_tables
from router import router as tasks_router
from contextlib import asynccontextmanager
#позволяет создавать контекст менеджер

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Удаляет таблицы перед запуском.
    Создает таблицы перед началом работы.
    Выполняет завершающие действия при выключении.
    """
    await delete_tables()
    print("База очищена")
    await create_tables()
    print("База готова к работе")
    yield
    print("Выключение")

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)

