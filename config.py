from dotenv import load_dotenv
import os

# Load variables from the .env file
load_dotenv()

# Access environment variables
bot_token = os.getenv("BOT_TOKEN")
host = os.getenv("HOST")