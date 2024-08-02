import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '../.env')
load_dotenv(dotenv_path)

owner_ids = os.getenv('OWNER_IDS')
token = os.getenv("TOKEN")