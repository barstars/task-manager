import datetime
import uuid

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import String

class Base(DeclarativeBase):
	"""
	The parent for all databases
	"""
	pass

class UsersBase(Base):
	__tablename__ = "users"

	id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
	username: Mapped[str] = mapped_column(String)
	email: Mapped[str] = mapped_column(String, unique=True)
	password_hash: Mapped[str] = mapped_column(String)

class SessionsBase(Base):
	__tablename__ = "sessions"

	id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
	user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"))