import uuid
from datetime import datetime, timedelta

from sqlalchemy import select, update, and_, not_, func

from models.tables import TasksBase

async def check_tasks():
    from database import get_db  # Импортируется здесь чтобы избежать циклических импортов
    async for db in get_db():
        print("Проверка началась...")
        now = datetime.now()

        # Обновляем задачи, которые просрочены и ещё не сделаны
        await db.execute(update(TasksBase).where(and_(
            not_(TasksBase.status.in_(["done", "expired"])),
            TasksBase.due_date < now)
        ).values(status="expired"))
        await db.commit()

        # Ищем задачи, у которых завтра прострочка
        tomorrow = now + timedelta(days=1)
        result = await db.execute(select(TasksBase).where(and_(
            not_(TasksBase.status.in_(["done", "expired"])),
            func.date(TasksBase.due_date) == tomorrow.date()
        )))
        tasks = result.scalars().all()
        for task in tasks:
            print("Завтра просрочка:", str(task.id))
        print("Проверка завершена.")
        break
