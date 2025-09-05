import logging
import asyncio
from pyrogram import Client, idle
from logging.handlers import RotatingFileHandler

# 🔹 Logger setup
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

# 🔹 Your Telegram API credentials
API_ID = 25519039
API_HASH = "1890ea8e01f2824e5827ee07cb6c51d3"
BOT_TOKEN = "8413663158:AAGWgLfNUji2l7weqw5JODMoA9ftL9XBWYo"

# 🔹 Plugins folder (handlers/commands go inside plugins/)
plugins = dict(root="plugins")

# 🔹 Initialize bot client
bot = Client(
    "StarkBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=plugins,
    workers=50
)

# 🔹 Async entrypoint
async def main():
    await bot.start()
    bot_info = await bot.get_me()
    LOGGER.info(f"🤖 Bot started successfully as @{bot_info.username}")
    await idle()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
    LOGGER.info("❌ Bot stopped")
