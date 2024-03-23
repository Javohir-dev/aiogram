import sqlite3 as sql


async def start_db() -> None:
    global db, cur
    db = sql.connect("aiogram.db")
    cur = db.cursor()

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS profile(
            user_id TEXT PRIMARY KEY,
            photo TEXT,
            age TEXT,
            name TEXT,
            description TEXT
        )
        """
    )
    db.commit()


async def create_profile(user_id) -> None:
    user = cur.execute(
        "SELECT 1 FROM profile WHERE user_id == '{key}'".format(key=user_id)
    ).fetchone()
    if not user:
        cur.execute(
            "INSERT INTO profile VALUES(?, ?, ?, ?, ?)",
            (user_id, "", "", "", ""),
        )
        db.commit()


async def edit_profile(state, user_id) -> None:
    async with state.proxy() as data:
        cur.execute(
            """
            UPDATE profile SET
                photo = '{}',
                age = '{}',
                description = '{}',
                name = '{}'
                WHERE user_id == '{}'
            """.format(
                data["photo"],
                data["age"],
                data["description"],
                data["name"],
                user_id,
            )
        )
        db.commit()
