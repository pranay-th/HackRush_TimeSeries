from flask import Flask, render_template, jsonify, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from plots import plot_time_series_for_region

app = Flask(__name__)

# Configure PostgreSQL database
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 'postgresql://neondb_owner:Ijov0mkf6Ohl@ep-damp-dust-a11bi2qp-pooler.ap-southeast-1.aws.neon.tech/neondb?sslmode=require'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy and Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import models
from models import Disease_Frequency, Drug_Sales, Disease, Region

# Route for Patient Records (Disease Frequency)
@app.route('/api/patient_records', methods=['GET'])
def patient_records():
    records = Disease_Frequency.query.all()
    data = [
        {'date': record.date, 'time': record.time, 'disease': Disease.query.get(record.diseaseId).name, 'region': Region.query.get(record.regionId).name}
        for record in records
    ]
    return jsonify(data)

# Route for Drug Consumption Records
@app.route('/api/drug_consumption', methods=['GET'])
def drug_consumption():
    records = Drug_Sales.query.all()
    data = [
        {'date': record.date, 'time': record.time, 'disease': Disease.query.get(record.diseaseId).name, 'region': Region.query.get(record.regionId).name}
        for record in records
    ]
    return jsonify(data)

# Route to serve time series plot image
@app.route('/plot')
def plot():
    image_path = plot_time_series_for_region()
    return send_file(image_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
