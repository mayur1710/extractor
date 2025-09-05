import os

class Config(object):
    # Always use environment variables; no default token
    BOT_TOKEN = os.environ.get("BOT_TOKEN")  
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    AUTH_USERS = os.environ.get("AUTH_USERS", "1411895712")  # optional default


