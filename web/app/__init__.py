import sys
import os
from flask import Flask

# Add the 'web' directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Print the sys.path for debugging
print("sys.path in __init__.py:", sys.path)

def create_app():
    app = Flask(__name__)

    # Set configuration paths
    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'uploads')
    app.config['PLOTS_FOLDER'] = os.path.join(app.root_path, 'static', 'plots')

    # Ensure the directories exist
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config['PLOTS_FOLDER'], exist_ok=True)

    # Register blueprints
    from .routes import main
    app.register_blueprint(main)

    return app