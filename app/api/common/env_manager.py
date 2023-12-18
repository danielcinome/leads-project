import os
from dotenv import load_dotenv

load_dotenv()

class EnvManager:
    SQLALCHEMY_DATABASE_URL: str = os.environ.get('SQLALCHEMY_DATABASE_URL')
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.environ.get('ACCESS_TOKEN_EXPIRE_MINUTES', 15))
    SECRET_KEY: str = os.environ.get('SECRET_KEY')
    ALGORITHM: str = os.environ.get('ALGORITHM', "HS256")
