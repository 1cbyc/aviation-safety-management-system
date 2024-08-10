from flask import Flask
from web.app.routes import main

app = Flask(__name__, template_folder='app/templates')  # Ensure this path is correct
# Configure the paths for file uploads and plot storage
app.config['UPLOAD_FOLDER'] = 'app/uploads'
app.config['PLOTS_FOLDER'] = 'app/static/plots'

app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)