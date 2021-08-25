import sqlite3
from datetime import datetime
import json


sql_transaction = []

connection = sqlite3.connect('data.db')
c = connection.cursor()


def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS parent_reply
    (parent_id TEXT PRIMARY KEY, comment_id TEXT UNIQUE, parent TEXT, 
    comment TEXT, subreddit TEXT, unix INT, score INT)""")


if __name__ == '__main__':
    create_table()
