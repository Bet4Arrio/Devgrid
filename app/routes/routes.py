import asyncio
from flask import jsonify
from app import app
from ..views import users

@app.route("/<id>", methods=['GET'])
def root(id):
    resp = users.get_request(id)
    return resp

@app.route("/", methods=['POST'])
async def city():
    return await users.post_cities()
