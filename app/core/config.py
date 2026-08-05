from fastapi import FastAPI 
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    database_url: str
   

settings = Settings()
app = FastAPI()
