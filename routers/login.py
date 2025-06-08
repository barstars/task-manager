from typing import AsyncGenerator

from fastapi import APIRouter, Depends, Cookie

router = APIRouter(
	prefix="/login",
	tags=["login"])

@router.post()