from re import U
from app import Sensor, WeatherUpdate
from app import db 
from app import app 
from datetime import datetime
def test_new_sensor():

    sensor = Sensor(name = "Sensor1", country = "Germany", city = "Berlin")


    assert sensor.name == "Sensor1"

    assert sensor.country == "Germany"
    
    assert sensor.city == "Berlin"

"""def test_transaction(db_session):
    row = db_session.query(Sensor).get(1)
    row.name = "testing"

    db_session.add(row)
    db_session.commit()"""

"""def test_new_Weather():
    sensor1 = Sensor(name = "Sensor1", country = "Germany", city = "Berlin")
    sensor = sensor1.query.get_or_404(id)
    date_object = datetime.date.today()

    update = WeatherUpdate(temperature = 10, humidity = 20, date_created = date_object, sensor = sensor)


    assert update.temperature == 10

    assert update.humidity == 20
    
    assert update.date_created == date_object

    assert update.sensor == sensor

"""
def test_home():

    response = app.test_client().get("/")
    assert response.status_code == 200

def test_home_fail():

    response = app.test_client().get("/home")
    assert response.status_code != 200

def test_update():
    response = app.test_client().get("/update/1")
    assert response.status_code == 200

def test_update_fail():
    response = app.test_client().get("/update/string")
    assert response.status_code != 200

def test_delete():
    response = app.test_client().get("/delete/1")
    assert response.status_code == 200

def test_delete():
    response = app.test_client().get("/delete/string")
    assert response.status_code != 200


def test_search():
    response = app.test_client().get("/search")
    assert response.status_code == 200
