from flask import jsonify
from flask import Flask, request
from connection import *

def get_available_desks(given_date):
    all_desks = []
    conn = create_connection()
    with conn:
        available_desks = get_all_available_desks_with_date(conn, given_date)
        for available_desk in available_desks:
            all_desks.append({"floor":available_desk[5], "desk_number":available_desk[6], "name":available_desk[7], "standing_desk":bool(available_desk[8]), "notes":available_desk[9], "full_day": bool(available_desk[11]), "available_from": available_desk[12], "available_to": available_desk[13]})
    return all_desks

def get_all_available_desks():
    all_desks = []
    conn = create_connection()
    with conn:
        # cur = conn.cursor()
        # cur.execute("SELECT date FROM available_desks GROUP BY date(date) ORDER BY date(date) ASC")
        # return cur.fetchall()

        all_dates = get_field_from_table(conn, "available_desks", "date")
        for given_date in all_dates:
            available_desks = get_all_available_desks_with_date(conn, given_date[0])
            given_date_data = []
            for available_desk in available_desks:
                given_date_data.append({"floor":available_desk[5], "desk_number":available_desk[6], "name":available_desk[7], "standing_desk":bool(available_desk[8]), "notes":available_desk[9], "full_day": bool(available_desk[11]), "available_from": available_desk[12], "available_to": available_desk[13]})
            all_desks.append({"date": given_date[0], "data": given_date_data})
    return all_desks

def get_all_available_desks_with_date(conn, date):
    cur = conn.cursor()
    cur.execute("select * from available_desks inner join all_desks on available_desks.all_desks_id=all_desks.desk_number inner join available_types on available_desks.available_types_id=available_types.id where date='"+date+"';")
    return cur.fetchall()


def create_available_desk(conn, available_desk):
    sql = ''' INSERT INTO available_desks(all_desks_id,available_types_id,date)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, available_desk)
    return cur.lastrowid
