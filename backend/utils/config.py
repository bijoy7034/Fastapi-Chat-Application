from dotenv import load_dotenv
import os


load_dotenv()

MONGO_URL = os.getenv('MONGO_URL')
MONGO_DB_NAME = os.getenv('MONGO_DB_NAME')
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')
SECRET_KEY=os.getenv('SECRET_KEY')
ALGORITHM = "HS256"
