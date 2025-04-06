import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set the backend service URL from environment variables
BACKEND_SERVICE_URL = os.getenv("BACKEND_SERVICE_URL", "http://localhost:8001")
