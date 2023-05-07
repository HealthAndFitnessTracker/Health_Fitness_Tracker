import psycopg2
from configs import Config

def get_db():
    conn = psycopg2.connect(Config.DATABASE_URL, sslmode='require')
    return conn
