import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
SECURE_API_TOKEN = os.getenv("SECURE_API_TOKEN")
API_TOKEN_IMEI = os.getenv("API_TOKEN_IMEI")
ALLOWED_USERS = set(map(int, os.getenv("ALLOWED_USERS", "").split(",")))
API_URL = "http://127.0.0.1:8000/api/check-imei"
