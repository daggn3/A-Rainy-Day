

# Rainy Day

## Project Description:
a web application created with python and flask. Database and querying created and controlled by SQLAlchemy.

UI in very basic HTML & CSS. This was to make visualisations easier.

## How to run:
if required, pip install the following using:
```pip install flask, sqlalchemy ```

the database already contains some dummy data, including sensors and weather data attached to those sensors. 

to add sensors, give it a name, a country and a city location. 

to update a sensor, click on any sensor to add a weather update to that sensor.

you can then see all weather updates in question and can add a temperature and humidity.

by default when adding a new weather update, it will grab the current time.

queries can be used from the command line, this can be done by running the following:
1. ```python.exe ```<br>
2. ```from app import db ```<br>
3. ```from app import Sensor, WeatherData```<br>
Queries can then be used by following the documentation at: 
[Select, Insert, Delete — Flask-SQLAlchemy Documentation (2.x) (palletsprojects.com)](https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/#querying-records)

An example query:
````WeatherUpdate.query.filter(WeatherUpdate.date_created > date(2021, 1, 1)).count````

This will find all weather updates that took place after the 1st of January 2021. 
