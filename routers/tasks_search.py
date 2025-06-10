from typing import AsyncGenerator, Optional

from fastapi import APIRouter, Depends, Cookie, Query

from models.view_datas import TaskDataView
from service.auth import is_user
from views.user_view import get_tasks_view, not_user, not_filter
from database import get_db

router = APIRouter(
	prefix="/searsh",
	tags=["searsh"])

@router.get("/all")
async def get_all_user_tasks_post(db: AsyncGenerator = Depends(get_db),
	jwt: str = Cookie(None)):

	user_id = await is_user(db, jwt)

	if user_id:
		taskView = TaskDataView(db)
		tasks = await taskView.get_all_user_tasks(user_id=user_id)
		return get_tasks_view(tasks)
	else:
		return not_user()

@router.get("/status")
async def get_all_user_tasks_post(db: AsyncGenerator = Depends(get_db),
	status: Optional[str] = Query(None),
	jwt: str = Cookie(None)):

	user_id = await is_user(db, jwt)

	if user_id:
		if status and (status in ["done", "in_progress", "new", "expired"]):
			taskView = TaskDataView(db)
			tasks = await taskView.get_status_filter_tasks(user_id=user_id, status=status)
			return get_tasks_view(tasks)
		else:
			return not_filter()
	else:
		return not_user()

@router.get("/sorted")
async def get_sort_by_duo_date(db: AsyncGenerator = Depends(get_db),
	sort_type: Optional[str] = Query(None),
	jwt: str = Cookie(None)):

	user_id = await is_user(db, jwt)
	
	if user_id:
		if sort_type and (sort_type in ["desc", "asc"]):
			taskView = TaskDataView(db)
			tasks = await taskView.get_sorting_by_due_date(user_id=user_id, sort_type=sort_type)
			if tasks or (tasks == []):
				return get_tasks_view(tasks)
			else:
				return not_filter()
		else:
			return not_filter()
	else:
		return not_user()

@router.get("/by")
async def get_search_by(db: AsyncGenerator = Depends(get_db),
	title: Optional[str] = Query(None),
	jwt: str = Cookie(None)):

	user_id = await is_user(db, jwt)
	
	if user_id:
		if title:
			taskView = TaskDataView(db)
			tasks = await taskView.get_by_title(user_id=user_id, title=title)
			if tasks or (tasks == []):
				return get_tasks_view(tasks)
			else:
				return not_filter()
		else:
			return not_filter()
	else:
		return not_user()