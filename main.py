from fastapi import FastAPI

from routers import register#, login, create_tasks, tasks_edit, tasks_search

app = FastAPI()

app.include_router(register.router)
# app.include_router(login.router)
# app.include_router(create_tasks.router)
# app.include_router(tasks_edit.router)
# app.include_router(tasks_search.router)