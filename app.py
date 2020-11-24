# import necessary libraries
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://xdpgmdhrnknqxl:4fc3642dabb4d67167f5ddbf940bfc499cea51caf1be2423e6bd7a9209d0500a@ec2-54-159-107-189.compute-1.amazonaws.com:5432/dd26aote6e71t3'

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Remove auto sort
app.config['JSON_SORT_KEYS'] = False

db = SQLAlchemy(app)

# Map table


class crime (db.Model):
    __tablename__ = 'crime_location'
    State = db.Column(db.String(200))
    City = db.Column(db.String(200), primary_key=True)
    Violent_Crime_Rate = db.Column(db.Float)
    Latitude = db.Column(db.Float)
    Longitude = db.Column(db.Float)

    def __init__(self, State, City, Violent_Crime_Rate, Latitude, Longitude):
        self.State = State
        self.City = City
        self.Violent_Crime_Rate = Violent_Crime_Rate
        self.Latitude = Latitude
        self.Longitude = Longitude
# Education table


class EducationCrime(db.Model):
    __tablename__ = 'crime_education'
    Location = db.Column(db.String(200), primary_key=True)
    none = db.Column(db.Float)
    high_school = db.Column(db.Float)
    associate = db.Column(db.Float)
    bachelor = db.Column(db.Float)
    graduate = db.Column(db.Float)

    def __init__(self, none, high_school, associate, bachelor, graduate):
        self.none = none
        self.high_school = high_school
        self.associate = associate
        self.bachelor = bachelor
        self.graduate = graduate
# Marital Status table


class MaritalStatusCrime(db.Model):
    __tablename__ = 'crime_maritalstatus'
    Location = db.Column(db.String(200), primary_key=True)
    Never_Marrieds = db.Column(db.Float)
    Marrieds = db.Column(db.Float)
    Divorceds = db.Column(db.Float)
    Separateds = db.Column(db.Float)
    Widoweds = db.Column(db.Float)

    def __init__(self, Never_Marrieds, Marrieds, Divorceds, Separateds, Widoweds):
        self.Never_Marrieds = Never_Marrieds
        self.Marrieds = Marrieds
        self.Divorceds = Divorceds
        self.Separateds = Separateds
        self.Widoweds = Widoweds

# Race table


class Race(db.Model):
    __tablename__ = 'crime_race'
    Location = db.Column(db.String(200), primary_key=True)
    Blacks = db.Column(db.Float)
    Asians = db.Column(db.Float)
    NativeHawaiian_PacificIslanders = db.Column(db.Float)
    Whites = db.Column(db.Float)
    Hispanics_Latinos = db.Column(db.Float)
    AmericanIndian_AlaskanNatives = db.Column(db.Float)
    Two_or_Mores = db.Column(db.Float)
    Others = db.Column(db.Float)

    def __init__(self, Blacks, Asians, NativeHawaiian_PacficicIslanders, Whites, Hispanics_Latinos, AmericanIndian_AlaskanNatives, Two_or_Mores, Others):
        self.Blacks = Blacks
        self.Asians = Asians
        self.NativeHawaiian_PacificIslanders = NativeHawaiian_PacficicIslanders
        self.Whites = Whites
        self.Hispanics_Latinos = Hispanics_Latinos
        self.AmericanIndian_AlaskanNatives = AmericanIndian_AlaskanNatives
        self.Two_or_Mores = Two_or_Mores
        self.Others = Others


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/map')
def map():

    results = db.session.query(
        crime.City, crime.Violent_Crime_Rate, crime.Latitude, crime.Longitude).all()
    City = [result[0] for result in results]
    Violent_Crime_Rate = [result[1]for result in results]
    Latitude = [result[2] for result in results]
    Longitude = [result[3] for result in results]

    location_data = [{
        "City": City,
        "Violent Crime Rate": Violent_Crime_Rate,
        "Latitude": Latitude,
        "Longitude": Longitude,
    }]
    return render_template("map.html", location_data=location_data)


@app.route("/education")
def education():
    return render_template("ed.html")


@app.route("/education-submit", methods=["GET", "POST"])
def ed_submit():
    if request.method == "POST":
        Location = request.form["search-form"]

    results = db.session.query(EducationCrime.Location, EducationCrime.none, EducationCrime.high_school,
                               EducationCrime.associate, EducationCrime.bachelor, EducationCrime.graduate).all()
    for result in results:
        if (result[0] == Location):
            none = result[1]
            high_school = result[2]
            associate = result[3]
            bachelor = result[4]
            graduate = result[5]
    location_data = [{
        "None": none,
        "High School": high_school,
        "Associate": associate,
        "Bachelor": bachelor,
        "Graduate": graduate,
    }]
    return render_template("ed_chart.html", location_data=location_data)


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

    results = db.session.query(MaritalStatusCrime.Location, MaritalStatusCrime.Never_Marrieds, MaritalStatusCrime.Marrieds,
                               MaritalStatusCrime.Divorceds, MaritalStatusCrime.Separateds, MaritalStatusCrime.Widoweds).all()
    for result in results:
        if (result[0] == Location):
            Never_Marrieds = result[1]
            Marrieds = result[2]
            Divorceds = result[3]
            Separateds = result[4]
            Widoweds = result[5]
    location_data = [{
        "Never Married": Never_Marrieds,
        "Married": Marrieds,
        "Divorced": Divorceds,
        "Separated": Separateds,
        "Widowed": Widoweds,
    }]
    return render_template("ms_chart.html", location_data=location_data)


@app.route("/ms-chart")
def marital_chart():
    return render_template("ms_chart.html")


@app.route("/race")
def race():
    return render_template("race.html")


@app.route("/race-submit", methods=["GET", "POST"])
def race_submit():
    if request.method == "POST":
        Location = request.form["search-form"]

    results = db.session.query(Race.Location, Race.Blacks, Race.Asians, Race.NativeHawaiian_PacificIslanders, Race.Whites,
                               Race.Hispanics_Latinos, Race.AmericanIndian_AlaskanNatives, Race.Two_or_Mores, Race.Others).all()
    for result in results:
        if (result[0] == Location):
            Black = result[1]
            Asian = result[2]
            NativeHawaiian_PacificIslander = result[3]
            White = result[4]
            Hispanic_Latino = result[5]
            AmericanIndian_AlaskanNative = result[6]
            Two_or_More = result[7]
            Other = result[8]
    location_data = [{
        'Black': Black,
        'Asian': Asian,
        'NativeHawaiian_PacificIslander':NativeHawaiian_PacificIslander,
        'White': White,
        'Hispanic_Latino': Hispanic_Latino,
        'AmericanIndian_AlaskanNative': AmericanIndian_AlaskanNative,
        'Two_or_More': Two_or_More,
        'Other': Other,
    }]
    return render_template("race_chart.html", location_data=location_data)

@app.route("/race-chart")
def race_chart():
    return render_template("race_chart.html")
    
if __name__ == "__main__":
    app.run()
