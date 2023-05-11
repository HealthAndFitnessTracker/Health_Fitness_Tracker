from database import get_db

class User:
    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password

    def register(self):
        conn = get_db()
        cur = conn.cursor()

        query = 'SELECT * FROM users WHERE email=%s'
        cur.execute(query, (self.email,))
        result = cur.fetchone()
        if result:
            raise ValueError('Email already exitst!')

        query = "INSERT INTO users (email, username, password) VALUES (%s, %s, %s)"
        cur.execute(query, (self.email, self.username, self.password))
        conn.commit()

        cur.close()
        conn.close()
        
    def login(email, password):
        conn = get_db()
        cur = conn.cursor()

        query = "SELECT * FROM users WHERE email=%s AND password=%s"
        cur.execute(query, (email, password))
        result = cur.fetchone()

        cur.close()
        conn.close()

        if result:
            return User(result[1], result[2], result[3])
        else:
            raise ValueError('User does not exitst!')
