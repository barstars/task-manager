from typing import AsyncGenerator
from uuid import UUID

from sqlalchemy import select

from .tables import TasksBase

class TaskDataView:
	def __init__(self, db: AsyncGenerator):
		self.db = db

	async def get_all_user_tasks(self, user_id:str):
		result = await self.db.execute(select(TasksBase).where(TasksBase.user_id == UUID(user_id)))
		currs = result.scalars().all()
		res = [await cur.get_info() for cur in currs]
		return res