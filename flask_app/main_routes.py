from flask import Blueprint, current_app
from config import Config
import flask.sessions
from flask_pyoidc.user_session import UserSession

main_bp = Blueprint('main_bp', __name__)
auth = current_app.auth


@main_bp.route('/', methods=['GET'])
@auth.oidc_auth(Config.PROVIDER_NAME1)
def index():
    """front page"""
    return f"welcome to the front page"


@main_bp.route('/about', methods=['GET'])
@auth.oidc_auth(Config.PROVIDER_NAME1)
def about():
    user_session = UserSession(flask.session)
    try:
        info = user_session.userinfo
        return f"things about you: {info}"
    except:
        return f"this user is a mystery"
