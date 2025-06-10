from typing import AsyncGenerator

from fastapi import APIRouter, Depends, Cookie

from models.crud import TaskCRUD
from models.schemas import UpdateTaskStatus
from service.auth import is_user
from service.JWT import decode_access_token
from views.user_view import updateTasks, not_user
from database import get_db

router = APIRouter(
	prefix="/update",
	tags=["update"])

@router.post("/in_progress")
async def update_task_status_in_progress_post(data: UpdateTaskStatus, db: AsyncGenerator = Depends(get_db),
	jwt: str = Cookie(None)):

	user_id = await is_user(db, jwt)

	if user_id:
		taskCrud = TaskCRUD(db)
		try:
			task_id = (await decode_access_token(data.id)).get("id")
			await taskCrud.update_status(task_id, status="in_progress")
			return updateTasks(True)
		except Exception as e:
			print(e)
			return updateTasks(False)
	else:
		return not_user()

@router.post("/done")
async def update_task_status_done_post(data: UpdateTaskStatus, db: AsyncGenerator = Depends(get_db),
	jwt: str = Cookie(None)):

	user_id = await is_user(db, jwt)

	if user_id:
		taskCrud = TaskCRUD(db)
		try:
			task_id = (await decode_access_token(data.id)).get("id")
			await taskCrud.update_status(task_id, status="done")
			return updateTasks(True)
		except Exception as e:
			print(e)
			return updateTasks(False)
	else:
		return not_user()