from flask import Blueprint
from flask import jsonify
from flask import Flask, render_template, request
from connection import create_desk, create_connection

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

    database = r"/Users/jakir/Google Drive/apache/hot-desking/hotDeskingDB.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        desk_id = create_desk(conn, desk)

    return str(desk_id)


# curl -d "floor=1&desk_number=1&name=user1&standing_desk=0&notes=none" -X POST http://localhost:5000/api/create_desk
