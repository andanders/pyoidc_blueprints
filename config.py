from os import urandom
import datetime

class Config():
    ISSUER1 = "https://YOUR_URL/auth/realms/test"
    CLIENT1 = "keycloak_test"
    SECRET = "if this is on Github, you are in trouble"
    PROVIDER_NAME1 = "keycloak"
    SERVER_NAME = 'localhost:5000'
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=7).total_seconds()
    DEBUG= True
    SECRET_KEY =  urandom(32)
    LOGOUT_URIS = ['http://localhost:5000/logout']