from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent  # app/core -> app -> ledger_api


class Settings(BaseSettings):
    database_url: str

    model_config = SettingsConfigDict(env_file=".env")
settings = Settings()

# print("hellofrom config") for debugging stuff
