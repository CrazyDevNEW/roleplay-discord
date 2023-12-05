import os
import logging

discord_api_token = os.environ.get("DISCORD_API_TOKEN")
db_dsn = os.environ.get("DB_DSN")
time_format = "%Y-%m-%d %H:%M:%S"
log_level = logging.INFO
