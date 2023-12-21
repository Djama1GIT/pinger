import os

from pydantic import field_validator
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    class Config:
        env_file = '.env'

    TOKEN: str = os.getenv('TOKEN')
    SITES: str = os.getenv('SITES')
    CHAT_ID: int = os.getenv('CHAT_ID')


settings = Settings()
settings.SITES = settings.SITES.split()