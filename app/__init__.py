from flask import Flask
from flask_cors import CORS
import os

def create_app():
    app = Flask(__name__)
    
    CORS(app)
    
    app.config['UPLOAD_FOLDER'] = "uploads"
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    from .routes import main
    app.register_blueprint(main)
    
    return app