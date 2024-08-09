# from flask import Flask
#
# def create_app():
#     app = Flask(__name__)
#     app.config['UPLOAD_FOLDER'] = 'data/uploads'
#     app.config['PLOTS_FOLDER'] = 'app/static/plots'
#
#     from .routes import main
#     app.register_blueprint(main)
#
#     return app

import os
from flask import Flask

app = Flask(__name__)

# to set configuration paths
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'uploads')
app.config['PLOTS_FOLDER'] = os.path.join(app.root_path, 'static', 'plots')

# to ensure the directories exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['PLOTS_FOLDER'], exist_ok=True)