import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv('.env')


class Settings(BaseSettings):
    # Comet ML
    COMET_ML_API_KEY: str = os.getenv("COMET_ML_API_KEY")
    COMET_ML_WORKSPACE: str = os.getenv("COMET_ML_WORKSPACE")

    # kafka configuration
    KAFKA_BOOTSTRAP_SERVER: str = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")

    class Config():
        case_sensitive = True


settings = Settings()
