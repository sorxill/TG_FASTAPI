from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    bot_token: SecretStr
    url_web: SecretStr
    db_name: SecretStr
    db_host: SecretStr
    db_port: SecretStr
    db_user: SecretStr
    db_pass: SecretStr

    model_config = SettingsConfigDict(
        env_file="../.env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings(_env_file="../.env")
