from flask import Flask, render_template

from flask import request
from flask_caching import Cache
from flask_cors import CORS, cross_origin
from flask_json import FlaskJSON, JsonError, json_response, as_json
from flask_bootstrap import Bootstrap
from connection import main as connect_to_db

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
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)

if __name__ == "__main__":
    app.run(debug=True)