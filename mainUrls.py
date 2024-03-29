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
    date = '2019-11-1'
    available_desks = get_available_desks(date)
    return render_template('index.html', available_desks=available_desks, date=date)

@app.route("/all-available-desks")
def all_available_desks():
    available_desks = get_all_available_desks()
    return render_template('all-available-desks.html', available_desks=available_desks)

@app.route("/all-desks")
def all_desks():
    desks_layed_out = all_desks_layed_out()
    return render_template('all-desks.html', desks_layed_out=desks_layed_out)

@app.route("/all-desks-with-people")
def all_desks_with_people():
    desks_layed_out = all_desks_layed_out()
    return render_template('all-desks-with-people.html', desks_layed_out=desks_layed_out)


if __name__ == "__main__":
    app.run(debug=True)
