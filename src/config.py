import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '../.env')
load_dotenv(dotenv_path)

owner_ids = [1139950107995934863]
test_token = os.getenv("TEST_TOKEN")
token = os.getenv("TOKEN")

class Color:
    default = 0x70a9ff
    green = 0x86ff74
    red = 0xff7474

class Media:
    pannel_banner = ""

class Loggers:
    guild = os.getenv("GUILD_LOG")

class Links:
    support = "https://discord.gg/ghouls"
    invite = "https://discord.com/api/oauth2/authorize?client_id=1269028379928039544&permissions=8&scope=bot"