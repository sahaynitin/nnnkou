
from sample_config import Config
from database.database import Database

pyrogram = Database(Config.DATABASE_URL, Config.SESSION_NAME)
