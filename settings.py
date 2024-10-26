import os
from pydantic_settings import BaseSettings, SettingsConfigDict

DOTENV = os.path.join(os.path.dirname(__file__), ".env")


class DataBaseConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=DOTENV, env_file_encoding="UTF 8")
    dbname: str = ""
    user: str = ""
    password: str = ""
    host: str = ""
    port: str = ""
    other_dbname: str = ""


database_config = DataBaseConfig()
