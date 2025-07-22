import datetime
import uuid

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from sqlalchemy import DateTime, ForeignKey, String

from service.JWT import create_access_token

class Base(DeclarativeBase):
	"""
	The parent for all databases
	"""
	pass

class TasksBase(Base):
	__tablename__ = "tasks"

	id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
	title: Mapped[str] = mapped_column(String)
	description: Mapped[str | None] = mapped_column(String, nullable=True)
	tags: Mapped[list | None] = mapped_column(ARRAY(String), nullable=True)
	status: Mapped[str] = mapped_column(String)
	due_date: Mapped[datetime.datetime] = mapped_column(DateTime)
	user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"))

	async def get_info(self):
		return {"id": await create_access_token({"id":str(self.id)}),
		"title": self.title,
		"description": self.description,
		"tags": self.tags,
		"status": self.status,
		"due_date": str(self.due_date)}