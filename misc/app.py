from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)

# Configure PostgreSQL database
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql://neondb_owner:Ijov0mkf6Ohl@ep-damp-dust-a11bi2qp-pooler.ap-southeast-1.aws.neon.tech/neondb?sslmode=require')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy and Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define models based on the schema
class Disease_Frequency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    diseaseId = db.Column(db.Integer, db.ForeignKey('disease.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    regionId = db.Column(db.Integer, db.ForeignKey('region.id'), nullable=False)

class Drug_Sales(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    diseaseId = db.Column(db.Integer, db.ForeignKey('disease.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    regionId = db.Column(db.Integer, db.ForeignKey('region.id'), nullable=False)

class Disease(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)

class Region(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)

# Route for Patient Records (Disease Frequency)
@app.route('/patient_records')
def patient_records():
    # Fetch data from the database
    records = Disease_Frequency.query.all()
    # Process data for time series analysis (you may need to adjust this based on your specific requirements)
    data = [{'date': record.date, 'time': record.time, 'disease': Disease.query.get(record.diseaseId).name, 'region': Region.query.get(record.regionId).name} for record in records]
    return render_template('patient_records.html', data=data)

# Route for Drug Consumption Records
@app.route('/drug_consumption')
def drug_consumption():
    # Fetch data from the database
    records = Drug_Sales.query.all()
    # Process data for time series analysis (you may need to adjust this based on your specific requirements)
    data = [{'date': record.date, 'time': record.time, 'disease': Disease.query.get(record.diseaseId).name, 'region': Region.query.get(record.regionId).name} for record in records]
    return render_template('drug_consumption.html', data=data)

# API route to get patient records data
@app.route('/api/patient_records', methods=['GET'])
def get_patient_records():
    records = Disease_Frequency.query.all()
    data = [{'date': record.date, 'time': record.time, 'disease': Disease.query.get(record.diseaseId).name, 'region': Region.query.get(record.regionId).name} for record in records]
    return jsonify(data)

# API route to get drug consumption data
@app.route('/api/drug_consumption', methods=['GET'])
def get_drug_consumption():
    records = Drug_Sales.query.all()
    data = [{'date': record.date, 'time': record.time, 'disease': Disease.query.get(record.diseaseId).name, 'region': Region.query.get(record.regionId).name} for record in records]
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)