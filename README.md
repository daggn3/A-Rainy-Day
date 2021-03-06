

# Rainy Day

## Project Description:
A web application created with python3 and flask. Database and querying created and controlled by SQLAlchemy.

UI in very basic HTML & CSS. This was to make visualisations easier.

## How to run:
**Please use python3.x to run this flask application.**
 
If required, pip install the following using:
```pip install flask, sqlalchemy, flask_sqlalchemy, datetime, webargs```

Requirements.txt contains all requirements on my machine, so maybe not a good idea to pip install that!

The database already contains some dummy data, including sensors and weather data attached to those sensors. 

To add sensors, give it a name, a country and a city location. 

To update a sensor, click on any sensor to add a weather update to that sensor.

You can then see all weather updates in question and can add a temperature and humidity.

By default when adding a new weather update, it will grab the current time.

Queries can be used from the command line, this can be done by running the following:
1. ```python3.exe ```<br>
2. ```from app import db ```<br>
3. ```from app import Sensor, WeatherData```<br>
4. ```from datetime import datetime```<br>
5. ```from from sqlalchemy.sql import func```<br>

Func can be used to express averages and means for data such as temperature and humidity. 

Queries can then be used by following the documentation at: 
[Select, Insert, Delete — Flask-SQLAlchemy Documentation (2.x) (palletsprojects.com)](https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/#querying-records)

*func.avg* can be used to query and retrieve average values for columns such as temperature and humidity.

Example queries:<br>
```WeatherUpdate.query.order_by(WeatherUpdate.id).all()```


Retrieves all weather updates, this will include Associated Sensor id, the temperature and the humidity.

````WeatherUpdate.query.filter(WeatherUpdate.date_created > date(2021, 1, 1)).count````

This will find the number weather updates that took place after the 1st of January 2021. 

## Features 

- A basic UI allowing Registration of Sensor with a name, a country and a city through an API call. 

- A basic UI to view weather updates and update individual sensor weather information through an API call. 

- Weather sensor querying through Flask & SQLAlchemy. 

## Data Flow Diagram

<img src="Flow.png" width="350" height="500" />

### Things I would include

- I created a basic UI for a searching weather information based on certain parameters but time constraints led me 
to leaving this implementation. Queries are then completed through the terminal. 

- I would of also loved to add more testing. Tests consist of basic unit tests to make sure routes work and also to test database functionality. 

- I Would have also liked to create a much more appealing UI with a frontend framework but as this wasn't necessary, the UI presented was sufficient. 
## Challenges I encountered
- This was my first time using flask with sqlalchemy so it was very much a learning on the job process.
If I had more time I would take a much more measured approach to database design with a more
Elegant implementation but for a first effort it was a great learning experience.

- Creating the relationship between the two tables was somewhat confusing but once I understood, creating updates was quite straightforward. 

- I did not get to do much testing beyond basic unit tests.

