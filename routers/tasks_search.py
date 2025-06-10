from typing import AsyncGenerator

from fastapi import APIRouter, Depends, Cookie

from models.view_datas import TaskDataView
from service.auth import is_user
from views.user_view import get_tasks_view, not_user
from database import get_db

router = APIRouter(
	prefix="/searsh",
	tags=["searsh"])

@router.post("/all")
async def get_all_user_tasks_post(db: AsyncGenerator = Depends(get_db),
	jwt: str = Cookie(None)):

	user_id = await is_user(db, jwt)

	if user_id:
		taskView = TaskDataView(db)
		tasks = await taskView.get_all_user_tasks(user_id=user_id)
		return get_tasks_view(tasks)
	else:
		return not_user()