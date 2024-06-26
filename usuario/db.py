import mysql.connector
from flask import current_app, g

def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host = current_app.config['DATABASE_HOST'],
            user = current_app.config['DATABASE_USER'],
            password = current_app.config['DATABASE_PASSWORD'],
            database = current_app.config['DATABASE']
        )
        g.c = g.db.cursor(dictionary=True)
    return g.db, g.c

def close_db():
    db = g.pop('db', None)
    if db is not None:
        db.close()