from typing import AsyncGenerator
import uuid

from sqlalchemy import select, update

from models.schemas import UserAdd, UserLogin, TaskAddForBase
from .tables import *
from service.password_hashing import hash_password, verify_password

class UserCRUD:
	def __init__(self, db: AsyncGenerator):
		self.db = db

	async def create(self, data: UserAdd):
		datas = data.model_dump()
		password = datas.pop("password")
		user = UsersBase(**datas)
		user.password_hash = hash_password(password)

		self.db.add(user)
		await self.db.commit()
		return user.id

	async def login(self, email:str, password:str):
		result = await self.db.execute(select(UsersBase).where(UsersBase.email == email))
		curr = result.scalars().first()

		if curr and  verify_password(password, curr.password_hash):
			return curr.id
		else:
			return False

class SessionCRUD:
	def __init__(self, db: AsyncGenerator):
		self.db = db

	async def create(self, user_id):
		if user_id:
			ses = SessionsBase(user_id=user_id)

			self.db.add(ses)
			await self.db.commit()
			return str(ses.id)
		else:
			return None

	async def get_by_id(self, id_:str):
		if id_:
			result = await self.db.execute(select(SessionsBase).where(SessionsBase.id == uuid.UUID(id_)))
			curr = result.scalars().first()
			if curr:
				return curr
			else:
				return False
		else:
			return False

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