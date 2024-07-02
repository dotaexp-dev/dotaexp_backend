from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


from app.settings import POSTGRES_FULL_URL


db_engine = create_async_engine(url=POSTGRES_FULL_URL)
async_session = async_sessionmaker(db_engine)
