from pyrogram import Client, filters

# ==========================
# Telegram API Credentials
# ==========================
API_ID = 25519039
API_HASH = "1890ea8e01f2824e5827ee07cb6c51d3"
BOT_TOKEN = "8413663158:AAGWgLfNUji217weqw5JODMoA9ftL9XBWYo"

# ==========================
# Create Bot Client
# ==========================
bot = Client(
    "extract17_bot",       # Session name (can be any string)
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# ==========================
# Handlers
# ==========================

# Start command
@bot.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("✅ Bot is alive! Send me a file or command to begin.")

# Simple ping command
@bot.on_message(filters.command("ping"))
async def ping(client, message):
    await message.reply_text("🏓 Pong!")

# Echo back text
@bot.on_message(filters.text & ~filters.command(["start", "ping"]))
async def echo(client, message):
    await message.reply_text(f"You said: {message.text}")

# ==========================
# Run Bot
# ==========================
if __name__ == "__main__":
    print("🚀 Bot is starting...")
    bot.run()
