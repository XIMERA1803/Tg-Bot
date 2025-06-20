import logging
import sqlite3
logger = logging.getLogger(__name__)
conn = sqlite3.connect("BD.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS PLAYERS(
    id INTEGER PRIMARY KEY,
    money INT,
    lvl_rod INT,
    lvl_bait INT)
''')
conn.commit()

def save_user(user_id, money, lvl_rod, lvl_bait):
    cursor.execute('''
        INSERT INTO PLAYERS(id, money, lvl_rod, lvl_bait)
        VALUES(?,?,?,?)
        ON CONFLICT(id) DO UPDATE SET
            money=excluded.money,
            lvl_rod=excluded.lvl_rod,
            lvl_bait=excluded.lvl_bait
    ''', (user_id, money, lvl_rod, lvl_bait))
    conn.commit()

def load_user(user_id):
    cursor.execute('''
        SELECT money, lvl_rod, lvl_bait FROM PLAYERS WHERE id = ?
    ''', (user_id,))
    return cursor.fetchone()


def del_user(user_id):
    cursor.execute('''
        DELETE FROM PLAYERS WHERE id=?
    ''', (user_id,))
    conn.commit()
