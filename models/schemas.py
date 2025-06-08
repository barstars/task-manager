from pydantic import BaseModel, field_validator
from datetime import datetime

class TaskAdd(BaseModel):
	title: str
	description: str
	tags: list
	due_date: str # Станет [True,datetime.datetime]

	@field_validator('due_date')
	def parse_date(cls, v) -> list:
		try:
			return [True,datetime.strptime(v, "%d.%m.%Y")]
		except ValueError:
			return [False, "Дата должна быть в формате ДД.ММ.ГГГГ"]

class TaskUpdate(BaseModel):
	id: str
	title: str
	description: str
	due_date: str # Станет [True,datetime.datetime]

	@field_validator('due_date')
	def parse_date(cls, v):
		try:
			return [True,datetime.strptime(v, "%d.%m.%Y")]
		except ValueError:
			return [False, "Дата должна быть в формате ДД.ММ.ГГГГ"]

class UserAdd(BaseModel):
	username: str
	email: str
	password: str