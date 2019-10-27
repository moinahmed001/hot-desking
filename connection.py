import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_desk(conn, desk):
    """
    Create a new row into the all_desks table
    :param conn:
    :param desk:
    :return: desk id
    """
    sql = ''' INSERT INTO all_desks(floor,desk_number,name,standing_desk,notes)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, desk)
    return cur.lastrowid

def create_available_desk(conn, available_desk):
    """
    Create a new row into the available_desks table
    :param conn:
    :param available_desk:
    :return: available_desk id
    """
    sql = ''' INSERT INTO available_desks(all_desks_id,available_types_id,date)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, available_desk)
    return cur.lastrowid

def main():
    database = r"/Users/jakir/Google Drive/apache/hot-desking/hotDeskingDB.db"

    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        print("success.")
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
