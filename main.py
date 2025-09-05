import logging
from logging.handlers import RotatingFileHandler
from pyrogram import Client, idle
import asyncio

# Your Telegram API credentials
API_ID = 25519039
API_HASH = "1890ea8e01f2824e5827ee07cb6c51d3"
BOT_TOKEN = "8413663158:AAE1YZH5DPOPS_x3z4zCzsFm3HtOMJW-AJQ"

# Logging setup
LOGGER = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler("log.txt", maxBytes=5000000, backupCount=10),
        logging.StreamHandler(),
    ],
)

# Plugins directory
plugins = dict(root="plugins")

# Initialize Bot Client
bot = Client(
    "extract17_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    sleep_threshold=20,
    plugins=plugins,
    workers=50
)

async def main():
    await bot.start()
    bot_info = await bot.get_me()
    LOGGER.info(f"🚀 Bot started as @{bot_info.username}")
    await idle()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
    LOGGER.info("🛑 Bot stopped.")
