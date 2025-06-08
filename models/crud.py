from typing import AsyncGenerator

from models.schemas import UserAdd
from .tables import Users, Sessions
from service.password_hashing import hash_password, verify_password

class UserCRUD:
	def __init__(self, db: AsyncGenerator):
		self.db = db

	async def create(self, data: UserAdd):
		datas = data.model_dump()
		password = datas.pop("password")
		user = Users(**datas)
		user.password_hash = hash_password(password)

		self.db.add(user)
		await self.db.commit()
		return user.id

class SessionCRUD:
	def __init__(self, db: AsyncGenerator):
		self.db = db

	async def create(self, user_id):
		if user_id == None:
			return None
			
		ses = Sessions(user_id=user_id)

		self.db.add(ses)
		await self.db.commit()
		return str(ses.id)