from flask import Flask
from routes.auth import auth_bp # example login blueprint

def create_app():
    app=Flask(__name__)
    app.secret_key="my_secret_key"
    
    app.register_blueprint(auth_bp)
    
    return app