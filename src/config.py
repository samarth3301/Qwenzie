import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '../.env')
load_dotenv(dotenv_path)

owner_ids = os.getenv('OWNER_IDS')
token = os.getenv("TOKEN")

class Color:
    default = 0x70a9ff

class Media:
    pannel_banner = ""