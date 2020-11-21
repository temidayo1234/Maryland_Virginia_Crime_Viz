import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
rds_connection_string = "postgres:MolovesTemi2020!@localhost:5432/md_va_crime_demo_db"
engine = create_engine(f'postgresql://{rds_connection_string}')

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
education = Base.classes.crime_education
income = Base.classes.crime_income
marital_status = Base.classes.crime_maritalstatus
population = Base.classes.crime_population
race = Base.classes.crime_race
#crime_rate = Base.classes.md_va_crime_rate
#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/crime_education<br/>"
        f"/api/v1.0/crime_income"
    )


@app.route("/api/v1.0/crime-education")
def crime_education():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    results = session.query(education).all()

    session.close()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))

    return jsonify(all_names)


@app.route("/api/v1.0/crime-income")
def crime_income():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of passenger data including the name, age, and sex of each passenger"""
    # Query all passengers
    results = session.query(income).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_passengers
    all_income = list(np.ravel(results))

    return jsonify(all_income)

if __name__ == '__main__':
    app.run(debug=True)
