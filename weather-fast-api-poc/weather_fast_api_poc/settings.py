from functools import lru_cache
#from pydantic_settings import BaseSettings
from pydantic import BaseSettings


class Settings(BaseSettings):
    debug: bool = False
    log_file: str = 'stdout'

    class Config:
        env_file = ".env"
'''
    model_config = {
        "env_file": ".env",
    }
'''


@lru_cache
def get_settings() -> Settings:
    return Settings()

