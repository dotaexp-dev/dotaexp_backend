from fastapi import APIRouter
from starlette.requests import Request

from app.core.steam.auth import get_steam_auth_redirect_link, parse_steam_id
from app.core.steam.users import get_steam_user_info
from app.core.users import create_or_update_steam_user
from app.schemas.api.auth import SteamOpenIDRedirectLink, SteamOpenIDResponse
from app.settings import STEAM_WEB_API_REDIRECT_LINK

auth_router = APIRouter(prefix='/auth')


@auth_router.get('/redirect_link')
async def auth_redirect_link_handler():
    return SteamOpenIDRedirectLink(
        redirect_url=get_steam_auth_redirect_link(
            STEAM_WEB_API_REDIRECT_LINK
        )
    )


@auth_router.get('/callback')
async def auth_callback_handler(request: Request):
    steam_id = parse_steam_id(dict(request.query_params))
    user_info = await get_steam_user_info(steam_id)
    response_data = SteamOpenIDResponse(**user_info['response']['players'][0])
    await create_or_update_steam_user(response_data)
    return response_data
