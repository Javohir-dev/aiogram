import sqlite3 as sql


async def start_db() -> None:
    global db, cur
    db = sql.connect("aiogram.db")
    cur = db.cursor()

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS profile(
        user_id TEXT PRIMARY KEY,
        full_name TEXT,
        skills TEXT,
        phone_number TEXT,
        time TEXT,
        goal TEXT)
        """
    )
    db.commit()


async def create_profile(user_id) -> None:
    user = cur.execute(
        "SELECT 1 FROM profile WHERE user_id == '{key}'".format(key=user_id)
    ).fetchone()
    if not user:
        cur.execute(
            "INSERT INTO profile VALUES(?, ?, ?, ?, ?, ?)",
            (user_id, "", "", "", "", ""),
        )
        db.commit()


async def edit_profile(state, user_id) -> None:
    async with state.proxy() as data:
        cur.execute(
            """
            UPDATE profile SET
                full_name = ?,
                skills = ?,
                phone_number = ?,
                time = ?,
                goal = ?,
                WHERE user_id == ?
            """,
            (
                data["full_name"],
                data["skills"],
                data["phone_number"],
                data["time"],
                data["goal"],
                user_id,
            ),
        )
        db.commit()
