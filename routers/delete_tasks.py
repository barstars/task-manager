from typing import AsyncGenerator, Optional

from fastapi import APIRouter, Depends, Cookie, Query

from models.crud import TaskCRUD
from models.schemas import DeleteTask
from service.auth import is_user
from service.JWT import decode_access_token
from views.user_view import not_user, delete_task_view
from database import get_db

router = APIRouter(
	prefix="/delete",
	tags=["delete"])

@router.delete("/")
async def deleteTask(data: DeleteTask,
	db: AsyncGenerator = Depends(get_db),
	jwt: str = Cookie(None)):

	user_id = await is_user(db, jwt)

	if user_id:
		taskCrud = TaskCRUD(db)
		task_id = (await decode_access_token(data.id)).get("id")
		result = await taskCrud.delete_task(task_id)
		return delete_task_view(result)
	else:
		return not_user()
