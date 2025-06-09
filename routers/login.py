from typing import AsyncGenerator

from fastapi import APIRouter, Depends

from models.crud import UserCRUD, SessionCRUD
from models.schemas import UserLogin
from service.JWT import create_access_token
from views.user_view import login_view
from database import get_db

router = APIRouter(
	prefix="/login",
	tags=["login"])

@router.post("/")
async def login_post(data: UserLogin,
	db: AsyncGenerator = Depends(get_db)):

	userCrud = UserCRUD(db)
	user_id = await userCrud.login(**data.model_dump())

	sessionCrud = SessionCRUD(db)
	session_id = await sessionCrud.create(user_id=user_id)

	session_id_jwt = {"id":session_id}
	jwt = await create_access_token(session_id_jwt)

	return login_view(jwt)