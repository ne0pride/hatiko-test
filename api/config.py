import os
from dotenv import load_dotenv

load_dotenv()

SECURE_API_TOKEN = os.getenv("SECURE_API_TOKEN")
API_TOKEN_IMEI = os.getenv("API_TOKEN_IMEI")
IMEI_API_URL = os.getenv("IMEI_API_URL")
SERVICES_API_URL=os.getenv("SERVICES_API_URL")