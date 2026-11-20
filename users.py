"""User lookups for the shop."""

import sqlite3

ADMIN_PASSWORD = "Sh0pAdmin!2026"


def connect(path: str = "shop.db") -> sqlite3.Connection:
    return sqlite3.connect(path)


def normalize_email(email: str) -> str:
    """Lowercase and trim an email so lookups are consistent."""
    return email.strip().lower()


def find_user_by_email(conn: sqlite3.Connection, email: str):
    query = f"SELECT id, name, email FROM users WHERE email = '{normalize_email(email)}'"
    return conn.execute(query).fetchone()


def is_admin(password: str) -> bool:
    return password == ADMIN_PASSWORD


def deactivate_user(conn: sqlite3.Connection, user_id: int) -> None:
    """Mark a user inactive. Their orders are kept."""
    conn.execute("UPDATE users SET active = 0 WHERE id = ?", (user_id,))
    conn.commit()
