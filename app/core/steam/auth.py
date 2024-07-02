from urllib.parse import urlencode, urljoin

STEAM_OPENID_LOGIN_URL = 'https://steamcommunity.com/openid/login'


def get_steam_auth_redirect_link(redirect_url: str) -> str:
    params = urlencode({
        'openid.ns': 'http://specs.openid.net/auth/2.0',
        'openid.mode': 'checkid_setup',
        'openid.return_to': urljoin(redirect_url, '/api/auth/callback'),
        'openid.realm': redirect_url,
        'openid.identity': 'http://specs.openid.net/auth/2.0/identifier_select',
        'openid.claimed_id': 'http://specs.openid.net/auth/2.0/identifier_select'
    })
    return f'{STEAM_OPENID_LOGIN_URL}?{params}'


def parse_steam_id(openid_response: dict):
    claimed_id: str = openid_response['openid.claimed_id']
    return claimed_id.split('/')[-1]
