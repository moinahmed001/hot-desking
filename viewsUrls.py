from flask import Blueprint

views_urls = Blueprint('views_urls', __name__)


@views_urls.route("/account")
def accountList():
    return "list of accounts"
