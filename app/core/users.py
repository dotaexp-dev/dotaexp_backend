from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import async_session
from app.models.users import User
from app.schemas.api.auth import SteamOpenIDResponse


async def get_user_by_steam_id(
    session: AsyncSession,
    steam_id: str
) -> User | None:
    query = await session.execute(
        select(User)
        .where(User.steam_id == steam_id)
        .limit(1)
    )
    return query.scalar_one_or_none()


async def update_user_by_steam_id(
    session: AsyncSession,
    steam_id: str,
    data: dict
):
    await session.execute(
        update(User)
        .where(User.steam_id == steam_id)
        .values(**data)
        .returning(User)
    )
    await session.commit()


async def create_or_update_steam_user(data: SteamOpenIDResponse) -> User:
    data_dict = data.model_dump()
    async with async_session() as session:
        user = await get_user_by_steam_id(session, data.steam_id)
        if not user:
            session.add(User(**data_dict))
            await session.commit()
        else:
            await update_user_by_steam_id(session, data.steam_id, data_dict)
        await session.refresh(user)
    return user
