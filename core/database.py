import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# Carga variables de entorno desde un archivo .env
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")

if not MONGO_URI or not DB_NAME:
    raise Exception("Las variables de entorno MONGO_URI y DB_NAME deben estar definidas")

client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]

def get_user_collection():
    return db.get_collection("users")
