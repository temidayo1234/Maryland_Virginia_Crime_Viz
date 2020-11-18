import psycopg2
import sys
from  flask import Flask,render_template
from flask import jsonify

#################################################
# Load CSV
#################################################

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
app = Flask(__name__)

@app.route('/')
def welcome():
    return (
        f"Welcome to our MD and VA Crime Data!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/startdate/enddate"
    )

   


if __name__ == '__main__':
    app.run()