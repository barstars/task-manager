from typing import AsyncGenerator
import uuid

from sqlalchemy import select

from .schemas import TaskAddForBase
from .tables import TasksBase

class TaskCRUD:
	def __init__(self, db: AsyncGenerator):
		self.db = db

	async def create(self, data:TaskAddForBase):
		task = TasksBase(**data.model_dump())

		self.db.add(task)
		await self.db.commit()
		return str(task.id)

	async def update_status(self, id_:str, status:str) -> bool:
		await self.db.execute(update(TasksBase).where(TasksBase.id == uuid.UUID(id_)).values(status=status))
		await self.db.commit()
		return True

	async def delete_task(self, id_):
		curr = await self.get_by_id(id_)
		if curr:
			await self.db.delete(curr)
			await self.db.commit()
			return True
		else:
			return False

	async def get_by_id(self, id_:str):
		if id_:
			result = await self.db.execute(select(TasksBase).where(TasksBase.id == uuid.UUID(id_)))
			curr = result.scalars().first()
			if curr:
				return curr
			else:
				return False
		else:
			return False