import os

from dotenv import load_dotenv


load_dotenv()

class Settings:
    project_name: str = "Capstone Project"
    api_key: str = os.getenv("API_KEY")
    jwt_secret_key: str = os.getenv("JWT_SECRET_KEY")
    jwt_algorithm: str = "HS256"
    redis_url: str = os.getenv("REDIS_URL")
    model_path: str = "app/models/model.pkl"


settings = Settings()