from typing import AsyncGenerator

from fastapi import APIRouter, Depends

from models.crud import UserCRUD, SessionCRUD
from models.schemas import UserAdd
from service.JWT import create_access_token
from views.user_view import auth_view
from database import get_db

router = APIRouter(
	prefix = "/register",
	tags = ["register"])

@router.post("/")
async def register_post(data: UserAdd,
	db: AsyncGenerator = Depends(get_db)):

	try:
		userCrud = UserCRUD(db)
		user_id = await userCrud.create(data=data)
	except Exception:
		user_id = None

	sessionCrud = SessionCRUD(db)
	session_id = await sessionCrud.create(user_id=user_id)
	session_id_jwt = {"id":session_id}
	jwt = await create_access_token(session_id_jwt)

	return auth_view(jwt)