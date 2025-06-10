from typing import AsyncGenerator
from datetime import datetime
import uuid

from fastapi import APIRouter, Depends, Cookie

from models.crud import TaskCRUD
from models.schemas import TaskAdd, TaskAddForBase
from service.JWT import create_access_token
from service.auth import is_user
from views.user_view import taskAdd_view
from database import get_db

router = APIRouter(
	prefix="/taskadd",
	tags=["taskadd"])

@router.post("/")
async def taskadd_post(data: TaskAdd,
	db: AsyncGenerator = Depends(get_db),
	jwt: str = Cookie(None)):

	user_id = await is_user(db, jwt)
	if user_id:

		if data.due_date < datetime.now():
			status = "expired"
		else:
			status = "new"

		data_for_base = TaskAddForBase(**data.model_dump(), status=status, user_id=uuid.UUID(user_id))

		taskCrud = TaskCRUD(db)
		task_id = await taskCrud.create(data_for_base)

		task_id_jwt = {"id":task_id}
		jwt = await create_access_token(task_id_jwt)
		return taskAdd_view(jwt)
	else:
		return taskAdd_view(None)