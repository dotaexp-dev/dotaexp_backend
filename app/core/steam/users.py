from urllib.parse import urljoin, urlencode

import aiohttp

from app.settings import STEAM_WEB_API_KEY

STEAM_API_URL = 'http://api.steampowered.com/'


async def steam_api_request(method: str, data: dict):
    url = urljoin(STEAM_API_URL, method)
    data.update(key=STEAM_WEB_API_KEY, format='json')
    params = urlencode(data)
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{url}?{params}') as response:
            # TODO: Обработка ошибок
            return await response.json()


async def get_steam_user_info(user_steam_id: str | int):
    return await steam_api_request(
        'ISteamUser/GetPlayerSummaries/v0002',
        {'steamids': [user_steam_id]}
    )


async def get_steam_user_friends_list(user_steam_id: str | int):
    return await steam_api_request(
        'ISteamUser/GetFriendList/v0001',
        {'steamid': user_steam_id}
    )
