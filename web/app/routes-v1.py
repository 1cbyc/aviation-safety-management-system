import os
from flask import Blueprint, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import pandas as pd
from src.data_ingestion import load_data, save_data
from src.data_preprocessing import clean_data, transform_data
from src.analysis import get_summary_statistics, get_safety_trends
from src.visualization import plot_safety_trends
from src.model import train_model

# app = Flask(__name__)
main = Blueprint('main', __name__)

UPLOAD_FOLDER = 'data/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@main.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            # to ensure the directory exists
            os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            return 'File uploaded successfully'
    return render_template('upload.html')

# maybe i should ditch this:
# @main.route('/', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         # to check if the file is in the request
#         if 'file' not in request.files:
#             return redirect(request.url)
#
#         file = request.files['file']
#         if file.filename == '':
#             return redirect(request.url)
#
#         if file:
#             filename = secure_filename(file.filename)
#             file_path = os.path.join('data/uploads', filename)
#             file.save(file_path)
#
#             # to process the file
#             df = load_data(file_path)
#             df = clean_data(df)
#             df = transform_data(df)
#
#             # to generate summary and trends
#             summary_stats = get_summary_statistics(df)
#             trends = get_safety_trends(df)
#
#             # to save the plot
#             plot_filename = f'safety_trends_{filename.split(".")[0]}.png'
#             plot_path = os.path.join('app/static/plots', plot_filename)
#             plot_safety_trends(trends, save_path=plot_path)
#
#             return render_template('results-v2.html', summary=summary_stats.to_html(), plot_filename=plot_filename)
#
#     return render_template('upload.html')


# @main.route('/download/<filename>')
# def download_file(filename):
#     return send_from_directory(directory='app/static/plots', path=filename)

@main.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(directory=current_app.config['PLOTS_FOLDER'], path=filename)