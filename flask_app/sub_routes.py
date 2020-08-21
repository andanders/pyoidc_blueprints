from flask import Blueprint, current_app
from config import Config

sub_bp = Blueprint('sub_bp', __name__)
auth = current_app.auth

@sub_bp.route('/aux', methods=['GET'])
@auth.oidc_auth(Config.PROVIDER_NAME1)
def index():
    """aux page"""
    return "auxiliary page"