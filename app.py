import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import psycopg2
from flask import Flask, jsonify
from flask import Flask, render_template


#################################################
# Database Setup
engine = create_engine('postgresql://postgres:Lekan011singer!@localhost/dmv')

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
crime = Base.classes.crime



#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return (
        f"Welcome to my Crime Data Visuals!<br/>"
        f"Available Routes:<br/>"
        f"/locations<br/>"
        f"/searches<br/>"
        
    )


@app.route("/locations")
def locations():
     # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    results = session.query(crime).all()

    session.close()

    # Convert list of tuples into normal list
    all_data = list(np.ravel(results))

    link = jsonify(all_data)
    return render_template('index.html',link=link)


# @app.route("/api/v1.0/search")
# def stations():
#     session = Session(engine)
#     """Return a list of stations."""
#     station_query = session.query(Station.name).all()
#     session.close()

#     # Unravel results into a 1D array and convert to a list
#     stations = list(np.ravel(station_query))
#     return jsonify(stations=stations)

if __name__ == '__main__':
    app.run(debug=True)