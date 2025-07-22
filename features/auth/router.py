from typing import AsyncGenerator

from fastapi import APIRouter, Depends

from .crud import UserCRUD, SessionCRUD
from .schemas import UserAdd, UserLogin
from service.JWT import create_access_token
from views.user_view import login_view
from database import get_db

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
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

	return register_view(jwt)


@router.post("/login")
async def login_post(data: UserLogin,
	db: AsyncGenerator = Depends(get_db)):

	userCrud = UserCRUD(db)
	user_id = await userCrud.login(**data.model_dump())

	sessionCrud = SessionCRUD(db)
	session_id = await sessionCrud.create(user_id=user_id)

	session_id_jwt = {"id":session_id}
	jwt = await create_access_token(session_id_jwt)

	return login_view(jwt)