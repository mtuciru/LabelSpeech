from pydantic import BaseSettings


class Settings(BaseSettings):
    JWT_SECRET: str
    JWT_ACCESS_EXPIRE: int = 5
    JWT_REFRESH_EXPIRE: int = 60
    JWT_REFRESH_LONG_EXPIRE: int = 12

    DB_ADDR: str = 'postgres'
    DB_PORT: int = 5432
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_NAME: str

    SERVER_ADDR: str = "0.0.0.0"
    SERVER_PORT: int = 8000
    SERVER_TEST: bool = False

    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_REGION: str = "us-east-1"
    AWS_HOST: str
    AWS_BUCKET: str

    ADMIN_EMAIL: str
    ADMIN_PASSWORD: str
    MAX_USERS_WITH_FRAGMENT: int = 2

    S3_TOKEN: str


settings = Settings()
