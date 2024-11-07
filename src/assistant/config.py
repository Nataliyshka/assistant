from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    base_url: str
    login_user: str
    password_user: str
    
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')
    
settings = Settings()