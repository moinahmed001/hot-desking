from flask import Blueprint
from flask import jsonify

api_urls = Blueprint('api_urls', __name__)

@api_urls.route('/api')
def load_config():
    base_url = "http://uat.config.sky.com"
    return jsonify(base_url=base_url)
    # return base_url
