from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    ENVIRONMENT: str

    class Config:
        env_file = ".env"


settings = Settings()
