import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

DATABASE_URL = os.getenv("DATABASE_URL")

SUPER_ADMIN_ID = os.getenv("SUPER_ADMIN_ID")
if SUPER_ADMIN_ID is not None:
    SUPER_ADMIN_ID = int(SUPER_ADMIN_ID)

WEBHOOK_URL = os.getenv("WEBHOOK_URL")
