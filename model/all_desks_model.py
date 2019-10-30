from flask import jsonify
from flask import Flask, request
from connection import *



def create_desk(conn, desk):
    sql = ''' INSERT INTO all_desks(floor,desk_number,name,standing_desk,notes)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, desk)
    return cur.lastrowid
