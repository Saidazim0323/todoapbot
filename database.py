import asyncpg
import os
from config import DATABASE_URL

async def connect_db():
    return await asyncpg.connect(DATABASE_URL)

async def create_tables():
    conn = await connect_db()

    await conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            user_id BIGINT UNIQUE,
            reminder_hour INT DEFAULT 9
        );
    """)

    await conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            user_id BIGINT,
            title TEXT,
            is_done BOOLEAN DEFAULT FALSE
        );
    """)

    await conn.execute("""
        CREATE TABLE IF NOT EXISTS habits (
            id SERIAL PRIMARY KEY,
            user_id BIGINT,
            habit TEXT
        );
    """)

    await conn.close()
