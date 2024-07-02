import uuid

from sqlalchemy import String, UUID
from sqlalchemy.orm import mapped_column, Mapped

from app.models.base import Base


class User(Base):
    """Модель пользователей."""

    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    steam_id: Mapped[str] = mapped_column(String(17), index=True, unique=True)
    username: Mapped[str] = mapped_column(String(32))
    avatar_url: Mapped[str] = mapped_column(String(200))
    avatar_medium_url: Mapped[str] = mapped_column(String(200))
    avatar_full_url: Mapped[str] = mapped_column(String(200))
