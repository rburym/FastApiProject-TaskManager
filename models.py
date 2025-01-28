from typing import Optional
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# создаем асинхронную БД для отправки запроса в БД

eng = create_async_engine(
    "sqlite+aiosqlite:///testdb.db"
)
# создание новой сессии для работы с бд
new_session = async_sessionmaker(eng, expire_on_commit=False)


class Model(DeclarativeBase):
    pass


class TaskOrm(Model):
    """задаем основные параметры"""
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True)
    #выдаем первичный ключ
    name: Mapped[str]
    descriprtion: Mapped[Optional[str]]


async def create_tables():
    """Функция для создания таблиц, взята из документации алхимии"""
    async with eng.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def delete_tables():
    """Функция для удаления таблиц"""
    async with eng.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)