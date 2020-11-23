# import necessary libraries
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://xdpgmdhrnknqxl:4fc3642dabb4d67167f5ddbf940bfc499cea51caf1be2423e6bd7a9209d0500a@ec2-54-159-107-189.compute-1.amazonaws.com:5432/dd26aote6e71t3'

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Remove auto sort 
app.config['JSON_SORT_KEYS'] = False

db = SQLAlchemy(app)

# Education table
class EducationCrime(db.Model):
    __tablename__='crime_education'
    Location = db.Column(db.String(200), primary_key=True)
    none = db.Column(db.Float)
    high_school = db.Column(db.Float)
    associate = db.Column(db.Float)
    bachelor = db.Column(db.Float)
    graduate = db.Column(db.Float)

    def __init__(self, none, high_school,associate, bachelor, graduate):
        self.none= none
        self.high_school= high_school
        self.associate=associate
        self.bachelor=bachelor
        self.graduate=graduate
# Marital Status tale
class MaritalStatusCrime(db.Model):
    __tablename__='crime_maritalstatus'
    Location = db.Column(db.String(200), primary_key=True)
    Never_Marrieds = db.Column(db.Float)
    Marrieds = db.Column(db.Float)
    Divorceds = db.Column(db.Float)
    Separateds = db.Column(db.Float)
    Widoweds = db.Column(db.Float)

    def __init__(self, Never_Marrieds, Marrieds,Divorceds, Separateds, Widoweds):
        self.Never_Marrieds= Never_Marrieds
        self.Marrieds= Marrieds
        self.Divorceds=Divorceds
        self.Separateds=Separateds
        self.Widoweds=Widoweds

@app.route('/')
def home():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/education <br/>"
        f"/marital-status <br/> "
    )

@app.route("/education")
def education():
    return render_template("ed.html")

@app.route("/education-submit", methods=["GET", "POST"])
def ed_submit():
    if request.method == "POST":
        Location = request.form["search-form"]
    
    results = db.session.query(EducationCrime.Location, EducationCrime.none, EducationCrime.high_school,EducationCrime.associate,EducationCrime.bachelor,EducationCrime.graduate).all() 
    for result in results:
        if (result[0]==Location):
            none= result[1]
            high_school= result[2]
            associate= result[3]
            bachelor = result[4]
            graduate = result[5]
    location_data = [{
        "None": none,
        "High School": high_school,
        "Associate": associate,
        "Bachelor": bachelor,
        "Graduate": graduate,
    }]
    return render_template("ed_chart.html",location_data=location_data)

@app.route("/ed-chart")   
def ed_chart():
    return render_template("ed_chart.html")

@app.route("/marital-status")
def marital_status():
    return render_template("ms.html")

@app.route("/marital-status-submit", methods=["GET", "POST"])
def marital_submit():
    if request.method == "POST":
        Location = request.form["search-form"]
    
    results = db.session.query(MaritalStatusCrime.Location, MaritalStatusCrime.Never_Marrieds, MaritalStatusCrime.Marrieds,MaritalStatusCrime.Divorceds,MaritalStatusCrime.Separateds,MaritalStatusCrime.Widoweds).all() 
    for result in results:
        if (result[0]==Location):
            Never_Marrieds= result[1]
            Marrieds= result[2]
            Divorceds= result[3]
            Separateds = result[4]
            Widoweds = result[5]
    location_data = [{
        "Never Married": Never_Marrieds,
        "Married": Marrieds,
        "Divorced": Divorceds,
        "Separateds": Separateds,
        "Widowed": Widoweds,
    }]
    return render_template("ms_chart.html",location_data=location_data)

@app.route("/ms-chart")   
def marital_chart():
    return render_template("ms_chart.html")

if __name__ == "__main__":
    app.run()
