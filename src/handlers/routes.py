import os
import csv
from flask import render_template, request
from pymongo import MongoClient
from werkzeug.utils import secure_filename

def routes_config(app):

    
    @app.route('/', methods=['GET', 'POST'])
    def get_data():
        return render_template('index.html')

    @app.route('/file', methods=['POST'])
    def save_file():
        # csvFile = request.files['file'].read()
        # test = csv.DictReader(csvFile)
        # return render_template('editFile.html', file=test)


        file = request.files['file'].read().decode('utf-8')
        reader = csv.DictReader(file)
        for row in reader:
            return render_template('editFile.html', file=row)
