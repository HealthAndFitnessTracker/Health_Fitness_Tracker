import os
import psycopg2

DATABASE_URL = 'postgres://rbstydqlceajzm:5d1c67294d8a93c866c8dd44db535ee01dc333778d4849dbd330b57c1ccce946@ec2-52-205-45-222.compute-1.amazonaws.com:5432/ddjfk3pcm4r9r9'

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
# 打开一个游标
cur = conn.cursor()

# 启用事务
conn.autocommit = False

# 尝试创建一个新表
try:
    cur.execute("""
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            email VARCHAR(50) UNIQUE NOT NULL,
            username VARCHAR(50) NOT NULL,
            password VARCHAR(50) NOT NULL
        );
    """)
    conn.commit()
    print("Table created successfully!")
except Exception as e:
    print("Error creating table: ", e)
    conn.rollback()

# 关闭游标和连接
cur.close()
conn.close()