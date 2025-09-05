import os
import asyncio
import logging
from logging.handlers import RotatingFileHandler
from pyrogram import Client, idle
import tgcrypto
from pyromod import listen

# Logging setup
LOGGER = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler("log.txt", maxBytes=5_000_000, backupCount=10),
        logging.StreamHandler(),
    ],
)

# Auth Users from environment variable (comma-separated IDs)
AUTH_USERS = [int(uid) for uid in os.environ.get("AUTH_USERS", "").split(",") if uid]

# Command prefixes
prefixes = ["/", "~", "?", "!"]

# Plugins directory
plugins = dict(root="plugins")

# Initialize Bot Client
bot = Client(
    "StarkBot",
    bot_token=os.environ.get("BOT_TOKEN"),
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH"),
    sleep_threshold=20,
    plugins=plugins,
    workers=5
)

async def main():
    try:
        await bot.start()
        bot_info = await bot.get_me()
        LOGGER.info(f"<--- @{bot_info.username} Started (c) STARKBOT --->")
        await idle()
    finally:
        await bot.stop()
        LOGGER.info("<---Bot Stopped--->")

if __name__ == "__main__":
    # Modern Python 3.11 approach
    asyncio.run(main())
