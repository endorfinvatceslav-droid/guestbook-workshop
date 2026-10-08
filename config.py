from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str
    greeting: str = "Добро пожаловать в гостевую книгу!"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
