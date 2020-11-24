import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
from flask import Flask, render_template

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
    return render_template('index.html')


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