import os
from flask import Blueprint, render_template, request, redirect, send_from_directory, current_app
from werkzeug.utils import secure_filename
import pandas as pd
from src.data_ingestion import load_data, save_data
from src.data_preprocessing import clean_data, transform_data
from src.analysis import get_summary_statistics, get_safety_trends
from src.visualization import plot_safety_trends
from src.model import train_model

main = Blueprint('main', __name__)

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
            os.makedirs(current_app.config['UPLOAD_FOLDER'], exist_ok=True)
            file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            return 'File uploaded successfully'
    return render_template('upload.html')

@main.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(directory=current_app.config['PLOTS_FOLDER'], path=filename)