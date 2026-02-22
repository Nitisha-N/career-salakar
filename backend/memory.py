import sqlite3
from datetime import datetime
import os

DB_FOLDER = "database"
DB_PATH = os.path.join(DB_FOLDER, "salakar.db")


def init_db():
    os.makedirs(DB_FOLDER, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            role TEXT NOT NULL,
            message TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def save_message(user_id, role, message):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO conversations (user_id, role, message, timestamp)
        VALUES (?, ?, ?, ?)
    """, (user_id, role, message, datetime.now().isoformat()))

    conn.commit()
    conn.close()


def get_conversation(user_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT role, message FROM conversations
        WHERE user_id = ?
        ORDER BY id ASC
    """, (user_id,))

    rows = cursor.fetchall()
    conn.close()

    return rows


def clear_conversation(user_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM conversations
        WHERE user_id = ?
    """, (user_id,))

    conn.commit()
    conn.close()
