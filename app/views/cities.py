import datetime
import time
import requests
from flask import request, jsonify
from app import db, API_KEY
from ..models.cities import Cities, city_schema, cities_schema

async def new_city(request_id: int, city_id:int):
    city = get_city_weather(request_id, city_id)
    try:
        return save_city(city)
    except:
        return None


def save_city(city):
    if city == None:
        return None

    db.session.add(city)
    db.session.commit()
    result = city_schema.dump(city)
    return result

def get_city_weather(request_id:int, city_id:int):
    unit = 'metric'
    uri = f"http://api.openweathermap.org/data/2.5/weather?id={city_id}&units={unit}&appid={API_KEY}"
    r = requests.get(uri)
    if r.status_code != requests.codes.ok:
        return None

    if r.status_code == 429:
        time.sleep(60)
        return get_city_weather(request_id, city_id)

    json = r.json()
    humidity = json['main']['humidity']
    temp = json['main']['temp']
    city = Cities(request_id, city_id, temp, humidity, datetime.datetime.now().now())
    return city