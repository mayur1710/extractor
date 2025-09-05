# MIT License
#
# Copyright (c) 2019-present Dan <https://github.com/delivrance>
# (License text omitted for brevity)

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
    workers=5  # reduced for free dyno limits
)

async def main():
    await bot.start()
    bot_info = await bot.get_me()
    LOGGER.info(f"<--- @{bot_info.username} Started (c) STARKBOT --->")
    await idle()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
    LOGGER.info(f"<---Bot Stopped--->")

