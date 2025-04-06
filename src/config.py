import os

from dotenv import load_dotenv

load_dotenv()

BACKEND_SERVICE_URL = os.getenv("BACKEND_SERVICE_URL", "http://localhost:8001")
