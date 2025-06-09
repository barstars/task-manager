import datetime
import uuid

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from sqlalchemy import DateTime, ForeignKey, String


class Base(DeclarativeBase):
	"""
	The parent for all databases
	"""
	pass

class UsersBase(Base):
	"""
	Database model for user
	"""
	__tablename__ = "users"

	id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
	username: Mapped[str] = mapped_column(String)
	email: Mapped[str] = mapped_column(String, unique=True)
	password_hash: Mapped[str] = mapped_column(String)

class TasksBase(Base):
	__tablename__ = "tasks"

	id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
	title: Mapped[str] = mapped_column(String)
	description: Mapped[str | None] = mapped_column(String, nullable=True)
	tags: Mapped[list | None] = mapped_column(ARRAY(String), nullable=True)
	status: Mapped[str] = mapped_column(String)
	due_date: Mapped[datetime.datetime] = mapped_column(DateTime)
	user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"))

class SessionsBase(Base):
	__tablename__ = "sessions"

	id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
	user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"))

