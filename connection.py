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


def create_desk(conn, desk):
    sql = ''' INSERT INTO all_desks(floor,desk_number,name,standing_desk,notes)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, desk)
    return cur.lastrowid

def create_available_desk(conn, available_desk):
    sql = ''' INSERT INTO available_desks(all_desks_id,available_types_id,date)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, available_desk)
    return cur.lastrowid




def get_all_fields_for_table(conn, table_name):
    cur = conn.cursor()
    cur.execute("SELECT * FROM "+table_name)
    return cur.fetchall()


def get_field_from_table(conn, table_name, field_name):
    cur = conn.cursor()
    cur.execute("SELECT "+field_name+" FROM "+table_name +" GROUP BY "+field_name)
    return cur.fetchall()

def get_all_available_desks_with_date(conn, date):
    cur = conn.cursor()
    cur.execute("select * from available_desks inner join all_desks on available_desks.all_desks_id=all_desks.desk_number inner join available_types on available_desks.available_types_id=available_types.id where date='"+date+"';")
    return cur.fetchall()


def main():
    conn = create_connection()
    if conn is not None:
        print("success.")
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
