from pydantic import BaseModel, field_validator
from datetime import datetime
import uuid

class TaskAdd(BaseModel):
	title: str
	description: str
	tags: list
	due_date: datetime

	@field_validator('due_date', mode='before')
	def parse_date(cls, v):
		if isinstance(v, datetime):
			return v
		try:
			return datetime.strptime(v, "%d.%m.%Y")
		except:
			raise ValueError("Дата должна быть в формате ДД.ММ.ГГГГ")

class TaskAddForBase(TaskAdd):
	title: str
	description: str
	tags: list
	status: str
	user_id: uuid.UUID
	due_date: datetime

class UpdateTaskStatus(BaseModel):
	id: str

class UserAdd(BaseModel):
	username: str
	email: str
	password: str

class UserLogin(BaseModel):
	email: str
	password: str