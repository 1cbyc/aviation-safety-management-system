from flask import Flask
from routes import main  # to import Blueprint

app = Flask(__name__)

# Configure the paths for file uploads and plot storage
app.config['UPLOAD_FOLDER'] = 'path/to/upload'
app.config['PLOTS_FOLDER'] = 'path/to/plots'

# Register the Blueprint
app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)