from flask import Flask
from flask_pyoidc.provider_configuration import ProviderConfiguration, ClientMetadata
from flask_pyoidc import OIDCAuthentication

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # auth setup
    ISSUER1 = app.config['ISSUER1']
    CLIENT1 = app.config['CLIENT1']
    SECRET = app.config['SECRET']
    PROVIDER_NAME1 = app.config['PROVIDER_NAME1']
    LOGOUT_URIS = app.config['LOGOUT_URIS']

    PROVIDER_CONFIG = ProviderConfiguration(
        issuer=ISSUER1,
        client_metadata=ClientMetadata(
            CLIENT1, SECRET,
            post_logout_redirect_uris=LOGOUT_URIS
        )
    )

    auth = OIDCAuthentication({PROVIDER_NAME1: PROVIDER_CONFIG})
    auth.init_app(app)

    app.auth = auth

    with app.app_context():

        #app.auth = auth # is it better to assign inside app_context?

        from flask_app import main_routes, sub_routes

        # init blueprints
        app.register_blueprint(main_routes.main_bp)
        app.register_blueprint(sub_routes.sub_bp)

        return app