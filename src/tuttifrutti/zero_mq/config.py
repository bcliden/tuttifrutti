from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        # `.env.prod` takes priority over `.env`
        env_file=(".env.example", ".env"),
        env_file_encoding="utf-8",
    )

    host: str = "*"
    port: str = "8674"
    loglevel: str = "info"
