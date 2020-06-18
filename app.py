import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#Create acces link to databas.
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect databse into classes
Base = automap_base()
Base.prepare(engine, reflect=True)

#Save refernces for tha table.
Measurement = Base.classes.measurement
Station = Base.classes.station

#create a session link from Python to our database 
session = Session(engine)

#Create flast instance.
app = Flask(__name__)
#Define the starting point.
@app.route('/')
def welcome():
    return(
    '''
    <h3>Welcome to the Climate Analysis API!</h3>
    <h3>Available Routes:</h3>
    <h4>/api/v1.0/precipitation</h4>
    <h4>/api/v1.0/stations</h4>
    <h4>/api/v1.0/tobs</h4>
    <h4>/api/v1.0/temp/start/end</h4>
    ''')
    
@app.route("/api/v1.0/precipitation")
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
	filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

@app.route("/api/v1.0/stations")
def stations():
   results = session.query(Station.station).all()
   stations = list(np.ravel(results))
   return jsonify(stations=stations)

@app.route("/api/v1.0/tobs")
def temp_monthly():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   results = session.query(Measurement.tobs).\
   filter(Measurement.station == 'USC00519281').\
   filter(Measurement.date >= prev_year).\
   all()
   temps = list(np.ravel(results))
   return jsonify(temps=temps)

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
   # to specify start & end dates: /api/v1.0/temp/2017-06-01/2017-06-30
   sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

   if not end:
      results = session.query(*sel).\
         filter(Measurement.date <= start).all()
      temps = list(np.ravel(results))
      jsonify(temps=temps)

   else:     
      results = session.query(*sel).\
      filter(Measurement.date >= start).\
      filter(Measurement.date <= end).all()
   temps = list(np.ravel(results))
   return jsonify(temps=temps)

if __name__ == '__main__':
    app.run(debug=True)