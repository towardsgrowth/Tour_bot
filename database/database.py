import sqlite3


class Database:
    def __init__(self, db_name: str = "main.db"):
        self.database = db_name

    def execute(self, sql, *args, commit: bool = False, fetchone: bool = False, fetchall: bool = False):
        with sqlite3.connect(self.database) as db:
            cursor = db.cursor()
            cursor.execute(sql, args)


            if commit:
                db.commit()
            elif fetchone:
                res = cursor.fetchone()
            elif fetchall:
                res = cursor.fetchall()
        return res


    def create_table_users(self):
        sql = '''CREATE TABLE IF NOT EXISTS users(
            telegram_id NOT NULL UNIQUE,
            full_name TEXT,
            phone_number VARCHAR(13),
            lang VARCHAR(3)
            )'''
        self.execute(sql, commit=True)

    def insert_telegram_id(self, telegram_id):
        sql = '''INSERT INTO users VALUES (?)'''
        self.execute(sql, telegram_id, commit=True)

    def update_lang(self, lang,  telegram_id):
        sql = '''UPDATE users SET lang = ? WHERE telegram_id = ?'''
        self.execute(sql, lang, telegram_id, commit=True)

    def get_user(self, telegram_id):
        sql  = '''SELECT * FROM users WHERE telegram_id = ?'''
        return self.execute(sql, telegram_id, fetchone=True)



