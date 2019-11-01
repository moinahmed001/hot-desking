from flask import Flask, render_template

from flask import request
from flask_caching import Cache
from flask_cors import CORS, cross_origin
from flask_json import FlaskJSON, JsonError, json_response, as_json
from flask_bootstrap import Bootstrap
from model.available_desks_model import *
from model.all_desks_model import *

import time
import json

from viewsUrls import views_urls
from apiUrls import api_urls

cache = Cache(config={'CACHE_TYPE': 'simple'})
app = Flask(__name__)
app.register_blueprint(views_urls)
app.register_blueprint(api_urls)

FlaskJSON(app)
Bootstrap(app)
CORS(app)
cache.init_app(app)

@app.route("/")
@app.route("/index")
def available_desks():
    # call api /api/available_desks?from=01012019&to=20012019
    date = '2019-11-1'
    available_desks = get_available_desks(date)
    return render_template('index.html', available_desks=available_desks, date=date)

@app.route("/all-available-desks")
def all_available_desks():
    available_desks = get_all_available_desks()
    return render_template('all-available-desks.html', available_desks=available_desks)

@app.route("/all-desks")
def all_desks():
    all_desks = get_all_desks()
    desks_layed_out = all_desks_layed_out()
    print(desks_layed_out)
    return render_template('all-desks.html', all_desks=all_desks, desks_layed_out=desks_layed_out)


def all_desks_layed_out():
    # layout = [4, 6, 6, 6, 6, 6, 6, 6]
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

if __name__ == "__main__":
    app.run(debug=True)
