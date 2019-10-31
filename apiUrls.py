from flask import Blueprint
from flask import jsonify
from flask import Flask, render_template, request
from connection import *
from flask import Response
from model.available_desks_model import *
from model.all_desks_model import *

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
        desk_id = create_desk(conn, desk)

    return str(desk_id)


@api_urls.route('/api/create_available_desk', methods=['POST'])
def api_create_available_desk():
    result = request.form

    all_desks_id = result['all_desks_id']
    available_types_id = result['available_types_id']
    date = result['date']


    available_desk = (int(all_desks_id), int(available_types_id), date)
    available_desk_id=0
    conn = create_connection()
    with conn:
        available_desk_id = create_available_desk(conn, available_desk)

    return str(available_desk_id)


# curl -d "floor=1&desk_number=2&name=user2&standing_desk=1&notes=none" -X POST http://localhost:5000/api/create_desk

@api_urls.route('/api/all_desks')
def api_all_desks():
    all_desks = get_all_desks()
    return Response(json.dumps(all_desks),  mimetype='application/json')

@api_urls.route('/api/all_available_desks')
def api_all_available_desks():
    all_desks = get_all_available_desks()
    return Response(json.dumps(all_desks),  mimetype='application/json')

@api_urls.route('/api/all_available_desks/<given_date>')
def api_all_available_desks_for_given_date(given_date):
    all_desks = get_available_desks(given_date)
    return Response(json.dumps(all_desks),  mimetype='application/json')
