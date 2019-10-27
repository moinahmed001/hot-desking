from flask import Blueprint
from flask import jsonify
from flask import Flask, render_template, request
from connection import create_desk, create_connection, get_all_fields_for_table, get_field_from_table, get_all_available_desks_with_date
from flask import Response

import json

api_urls = Blueprint('api_urls', __name__)

@api_urls.route('/api/create_desk', methods=['POST'])
def api_create_desk():
    result = request.form

    floor = result['floor']
    desk_number = result['desk_number']
    name = result['name']
    standing_desk = result['standing_desk']
    notes = result['notes']

    desk = (int(floor), int(desk_number), name, int(standing_desk), notes)
    desk_id=0
    conn = create_connection()
    with conn:
        desk_id = create_desk(conn, result)

    return str(desk_id)


# curl -d "floor=1&desk_number=2&name=user2&standing_desk=1&notes=none" -X POST http://localhost:5000/api/create_desk

@api_urls.route('/api/all_desks')
def api_all_desks():
    all_desks = []
    conn = create_connection()
    with conn:
        desks = get_all_fields_for_table(conn, "all_desks")
        for desk in desks:
            all_desks.append({"floor":desk[1], "desk_number":desk[2], "name":desk[3], "standing_desk":bool(desk[4]), "notes":desk[5]})

    return Response(json.dumps(all_desks),  mimetype='application/json')

@api_urls.route('/api/all_available_desks')
def api_all_available_desks():
    all_desks = []
    conn = create_connection()
    with conn:
        all_dates = get_field_from_table(conn, "available_desks", "date")
        for given_date in all_dates:
            print(given_date[0])
            available_desks = get_all_available_desks_with_date(conn, given_date[0])
            given_date_data = []
            for available_desk in available_desks:
                given_date_data.append({"floor":available_desk[5], "desk_number":available_desk[6], "name":available_desk[7], "standing_desk":bool(available_desk[8]), "notes":available_desk[9], "full_day": bool(available_desk[11]), "available_from": available_desk[12], "available_to": available_desk[13]})
            all_desks.append({"date": given_date[0], "data": given_date_data})

    return Response(json.dumps(all_desks),  mimetype='application/json')

@api_urls.route('/api/all_available_desks/<given_date>')
def api_all_available_desks_for_given_date(given_date):
    all_desks = []
    conn = create_connection()
    with conn:
        available_desks = get_all_available_desks_with_date(conn, given_date)
        for available_desk in available_desks:
            all_desks.append({"floor":available_desk[5], "desk_number":available_desk[6], "name":available_desk[7], "standing_desk":bool(available_desk[8]), "notes":available_desk[9], "full_day": bool(available_desk[11]), "available_from": available_desk[12], "available_to": available_desk[13]})

    return Response(json.dumps(all_desks),  mimetype='application/json')
