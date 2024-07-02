from fastapi import FastAPI

from app.routes.auth import auth_router


app = FastAPI(
    title='DotaExp',
    root_path='/api'
)
app.include_router(auth_router)
