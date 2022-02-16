from webargs import flaskparser, fields
from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from importlib_metadata import Sectioned

"""
from jinja2 import TemplateError
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
"""

## Start of our flask application 
##will be added to heroku

# Create my flask app
app = Flask(__name__)

# Create the location of the SQLlite Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# Suppress deprecation warning
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# to be used for input validation but did not have time to get
# webargs working 
"""SENSOR_ARGS = {
    'name': fields.Str(required=True),
    'country': fields.Str(required=True),
    'city': fields.Str(required=True),
}

"""
#Our sensor database model
# Requires a name, a country and a city
# Also establishes a relationship with the weather update database

class Sensor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    country = db.Column(db.String(40))
    city = db.Column(db.String(40))
    #date_created = db.Column(db.DateTime)
    weather = db.relationship(
        "WeatherUpdate", backref="sensor", lazy=True,
    )

    def __repr__(self):
        return f'<Sensor: {self.name}>'

# Our weather update database model
# Requires a temperature, humidity and a date created
# We also take in the sensor id from our Sensor database
# This allows us to create weather updates on a per sensor basis

class WeatherUpdate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Integer)
    humidity = db.Column(db.Integer)
    date_created = db.Column(db.DateTime)
    sensor_id = db.Column(db.Integer, db.ForeignKey("sensor.id"))
    
    def __repr__(self):
        return f'<WeatherUpdate: {self.id}>'


# Route to our home page

@app.route("/", methods=["POST", "GET"])

#function to take in a form containing our sensor data and add it to our database

def index():
    if request.method == "POST":
        
        
        sensor_name = request.form["name"]
        sensor_country = request.form["country"]
        sensor_city = request.form["city"]
        new_sensor = Sensor(name = sensor_name, country=sensor_country, city=sensor_city)

        try:
            db.session.add(new_sensor)
            db.session.commit()
            return redirect("/")
        except:
            return "unexpected error"
        
    else:
            sensors = Sensor.query.order_by(Sensor.id).all()
            return render_template("index.html", sensors=sensors)



@app.route("/delete/<int:id>")

#function to delete a sensor based on its id
# contains exception handling 
def delete(id):
    sensor_del = Sensor.query.get_or_404(id)

    try:
        db.session.delete(sensor_del)
        db.session.commit()
        return redirect("/")
    except:
        return "there was a problem deleting this sensor record"



@app.route('/update/<int:id>', methods=['GET', 'POST'])

# Function to create a weather update
# this takes in a temperature and a humidity 
# creates a WeatherUpdate entry tied to the Sensor's id that was selected

def update(id):
    #sensor = Sensor.query.get_or_404(id)
    sensor = Sensor.query.get_or_404(id)


    if request.method == 'POST':
        temperature = request.form['temperature']
        humidity = request.form['humidity']
        time = datetime.now()
        
        new_update = WeatherUpdate(temperature = temperature, humidity=humidity, date_created=time, sensor=sensor)
        try:
            db.session.add(new_update)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating the weather'

    else:
        weathers = WeatherUpdate.query.order_by(WeatherUpdate.date_created).all()
        return render_template('update.html', sensor=sensor, weathers = weathers)


# Could not be implemented in time
# this would be a UI version of querying weather updates based on a Sensor's ID 
# and various parameters such as time and option 
@app.route("/search", methods=["GET", "POST"])
def search():
    sensors = Sensor.query.order_by(Sensor.id).all()
    return render_template("search.html", sensors=sensors)

if __name__ == "__main__":
    app.run(debug=True)