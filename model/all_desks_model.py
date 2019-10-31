from flask import jsonify
from flask import Flask, request
from connection import *


def get_all_desks():
    all_desks = []
    conn = create_connection()
    with conn:
        desks = get_all_fields_for_table(conn, "all_desks")
        for desk in desks:
            all_desks.append({"floor":desk[1], "desk_number":desk[2], "name":desk[3], "standing_desk":bool(desk[4]), "notes":desk[5]})
    return all_desks

def create_desk(conn, desk):
    sql = ''' INSERT INTO all_desks(floor,desk_number,name,standing_desk,notes)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, desk)
    return cur.lastrowid
