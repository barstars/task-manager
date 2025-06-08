from fastapi import FastAPI

from routers import auth, create_tasks, tasks_edit, tasks_search

app = FastAPI()

app.include_router(auth.router)
app.include_router(create_tasks.router)
app.include_router(tasks_edit.router)
app.include_router(tasks_search.router)