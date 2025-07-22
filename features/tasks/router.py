from fastapi import APIRouter
from . import endpiont_add

admin_router = APIRouter(prefix="/task", tags=["task"])

admin_router.include_router(endpiont_add.router)
