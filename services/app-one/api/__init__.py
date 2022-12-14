from flask import Flask, jsonify
from .helpers.helpers import set_configuration
import os


def create_app():
    app = Flask(__name__)
    
    set_configuration(app)
    
    @app.route('/')
    def health_check():
        """Check if application is up."""
        return jsonify({'Hello': 'From flask app-one!'}), 200
    
    app.shell_context_processor({"app": app})

    return app
