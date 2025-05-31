from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    api_token: str = Field(default="", alias="API_TOKEN")
    api_base_url: str = Field(default="https://lksh-enter.ru", alias="API_BASE_URL")
    reason: str = Field(default="reason", alias="REASON")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


settings = Settings()
