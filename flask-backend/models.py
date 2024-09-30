from app import db

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
