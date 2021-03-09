import psycopg2
from psycopg2.extras import DictCursor

conn = psycopg2.connect("postgres://mzqzzqbbqshuyu:8dac9f5ddbfbc9f7556554c9d4d7b101acc45c7b2d8bce1c9ae90931f464c22f@ec2-54-205-61-191.compute-1.amazonaws.com:5432/d55vjv88et7bmh", 
                            cursor_factory=DictCursor)
cur = conn.cursor()

def check_table():
    cur.execute("SELECT * FROM registers")
    rows = cur.fetchall()

    print(rows)


def delete_table():
    cur.execute("DROP TABLE users;")
    conn.commit()
    cur.execute("DROP TABLE registers;")
    conn.commit()

    print("Done")

