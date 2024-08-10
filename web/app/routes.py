import os

import matplotlib.pyplot as plt
from flask import Blueprint, render_template, request, redirect, send_from_directory, current_app
from werkzeug.utils import secure_filename

from src.analysis import get_summary_statistics, get_safety_trends
from src.data_ingestion import load_data
from src.data_preprocessing import clean_data, transform_data
from src.visualization import plot_safety_trends

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
            file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)

            try:
                # Ensure the directory exists
                os.makedirs(current_app.config['UPLOAD_FOLDER'], exist_ok=True)
                os.makedirs(current_app.config['PLOTS_FOLDER'], exist_ok=True)

                file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)

                # Load and process the data
                df = load_data(file_path)
                df = clean_data(df)
                df = transform_data(df)

                # Generate summary statistics and safety trends
                summary_stats = get_summary_statistics(df)
                trends = get_safety_trends(df)

                # Plot and save the safety trends graph
                plot_filename = f'safety_trends_{filename.split(".")[0]}.png'
                plot_path = os.path.join(current_app.config['PLOTS_FOLDER'], plot_filename)
                plot_safety_trends(trends)  # Plot the trends
                plt.savefig(plot_path)  # Save the plot manually
                plt.close()  # Close the plot to free up memory

                # Return a link to download the generated plot
                return render_template('results.html', summary=summary_stats.to_html(), plot_filename=plot_filename)
            except Exception as e:
                return str(e), 500

    return render_template('upload.html')

@main.route('/download/<filename>')
def download_file(filename):
    try:
        return send_from_directory(directory=current_app.config['PLOTS_FOLDER'], path=filename)
    except Exception as e:
        return str(e), 500