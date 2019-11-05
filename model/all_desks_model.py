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

def all_desks_layed_out():
    all_desks = get_all_desks()

    return [{'one': [fetch_desk(all_desks, 70, 66), fetch_desk(all_desks, 74, 70)]},
    {'two': [fetch_desk(all_desks, 80, 74), fetch_desk(all_desks, 86, 80)]},
    {'three': [fetch_desk(all_desks, 92, 86), fetch_desk(all_desks, 98, 92)]},
    {'four': [fetch_desk(all_desks, 104, 98), fetch_desk(all_desks, 110, 104)]},
    {'six': [fetch_desk(all_desks, 116, 110), fetch_desk(all_desks, 122, 116)]},
    {'seven': [fetch_desk(all_desks, 128, 122), fetch_desk(all_desks, 134, 128)]},
    {'eight': [fetch_desk(all_desks, 140, 134), fetch_desk(all_desks, 146, 140)]},
    {'nine': [fetch_desk(all_desks, 152, 146), fetch_desk(all_desks, 158, 152)]}
     ]

def fetch_desk(all_desks, start, end_number):
    desks = []
    for i in range(start, end_number, -1):
        for desk in all_desks:
            if(desk['desk_number'] == i):
                desks.append(desk)
    return desks
