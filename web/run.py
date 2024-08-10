from flask import Flask
from routes import main  # to import Blueprint

app = Flask(__name__)

# Configure the paths for file uploads and plot storage
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['PLOTS_FOLDER'] = 'static/plots'
# app.config['UPLOAD_FOLDER'] = 'web/app/uploads'
# app.config['PLOTS_FOLDER'] = 'web/app/static/plots'

# Register the Blueprint
app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)