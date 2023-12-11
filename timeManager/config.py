# Using a virtual environment (venv)
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access environment variables
HEMIS_KEY = os.getenv("HEMIS_KEY")  # Hemis Token
DJANGO_KEY = os.getenv("DJANGO_KEY")  # Django Token