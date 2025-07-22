from pydantic import BaseModel

class UserAdd(BaseModel):
	username: str
	email: str
	password: str

class UserLogin(BaseModel):
	email: str
	password: str