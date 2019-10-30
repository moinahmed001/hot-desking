import sqlite3
from sqlite3 import Error


def create_connection():
    db_file = r"/Users/mah54/Google Drive/apache/hot-desking/hotDeskingDB.db"
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def get_all_fields_for_table(conn, table_name):
    cur = conn.cursor()
    cur.execute("SELECT * FROM "+table_name)
    return cur.fetchall()


def get_field_from_table(conn, table_name, field_name):
    cur = conn.cursor()
    cur.execute("SELECT "+field_name+" FROM "+table_name +" GROUP BY "+field_name)
    return cur.fetchall()


def main():
    conn = create_connection()
    if conn is not None:
        print("success.")
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
