from functools import lru_cache
#from pydantic_settings import BaseSettings
from pydantic import BaseSettings
import os

from dotenv import load_dotenv
load_dotenv("dev.env")


class Settings(BaseSettings):
    debug: bool = False
    log_file: str = 'stdout'
    openweather_api_key: str = os.getenv("OPENWEATHER_API_KEY")
"""
    class Config:
        env_file = "dev.env"
"""


@lru_cache
def get_settings() -> Settings:
    return Settings()

settings = get_settings()
print(settings.openweather_api_key)

