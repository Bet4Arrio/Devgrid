import datetime
import asyncio

from pprint import pprint
import re
from flask import request, jsonify
from app import db
from ..models.users import User_requests, user_requests_schema, user_request_schema
from ..models.cities import Cities, city_schema, cities_schema
from .cities import new_city

async def post_cities():
    user_req_id = request.json['id']
    time  = datetime.datetime.now()
    cities = request.json['cities']
    num_cities = len(cities)
    req = request_by_id(user_req_id)
    if req:
        return jsonify({'message': 'ID already exists', 'data': {}})
    
    req = User_requests(user_req_id, num_cities, time)
    
    try:
        result = save_request(req)
        tasks = []
        for city in cities:
            task = asyncio.create_task(new_city(user_req_id, city))
            tasks.append(task)
        cit = await asyncio.gather(*tasks)
        return jsonify({'message': 'successfully registered', 'data': {'session': result, 'cities':cit}}), 201
    except:
        return jsonify({'message': 'unable to create', 'data': {}}), 500

def save_request(req):
    db.session.add(req)
    db.session.commit()
    result =  user_request_schema.dump(req)
    return result

def get_request(id):
    req = get_cities_by_user(id)
    if req:
        result = cities_schema.dump(req)
        user_req = user_request_schema.dump(request_by_id(id))
        pct = (len(result)/user_req["num_cities"])*100
        return jsonify({'message': 'Process status', 'data':{'complete percent': f'{pct}%', 'cities':result}})
    return jsonify({'message': 'ID do not exists', 'data': {}})



def get_cities_by_user(user_id:int):
    try:
        return Cities.query.filter(Cities.user_request_id == user_id).all()
    except:
        return None



def request_by_id(id:int):
    try:
        return User_requests.query.filter(User_requests.id == id).one()
    except:
        return None