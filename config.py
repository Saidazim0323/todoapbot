import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # https://your-app.onrender.com/
WEBAPP_HOST = "0.0.0.0"
WEBAPP_PORT = int(os.getenv("PORT", 8000))

DEFAULT_REMINDER_HOUR = int(os.getenv("DEFAULT_REMINDER_HOUR", 9))
ADMIN_ID = int(os.getenv("ADMIN_ID", 0))
DATABASE_URL = os.getenv("DATABASE_URL")  # Postgres URL
