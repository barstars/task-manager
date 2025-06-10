from contextlib import asynccontextmanager

from fastapi import FastAPI
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from util.check_due_date import check_tasks

from routers import register, login, create_tasks, tasks_search, update_task, delete_tasks

@asynccontextmanager
async def lifespan(app: FastAPI):
	scheduler = AsyncIOScheduler()
	scheduler.add_job(check_tasks, CronTrigger(hour=0, minute=0))  # Каждый день в 00:00
	scheduler.start()
	yield

app = FastAPI(lifespan=lifespan)

app.include_router(register.router)
app.include_router(login.router)
app.include_router(create_tasks.router)
app.include_router(update_task.router)
app.include_router(tasks_search.router)
app.include_router(delete_tasks.router)