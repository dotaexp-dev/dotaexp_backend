from pydantic import BaseModel, Field


class SteamOpenIDRedirectLink(BaseModel):
    redirect_url: str


class SteamOpenIDResponse(BaseModel):
    steam_id: str = Field(alias='steamid')
    username: str = Field(alias='personaname')
    avatar_url: str = Field(alias='avatar')
    avatar_medium_url: str = Field(alias='avatarmedium')
    avatar_full_url: str = Field(alias='avatarfull')
