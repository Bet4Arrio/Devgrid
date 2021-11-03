import datetime
from app import db, ma

class User_requests(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    num_cities= db.Column(db.Integer)
    time = db.Column(db.DateTime)
    
    def __init__(self, id:int, num_cities:int, time:datetime) -> None:
        self.num_cities:int = num_cities 
        self.id:int = id
        self.time:datetime = time

class User_requestsSchema(ma.Schema):
    class Meta: 
        fields = ('id', 'num_cities','time')

user_request_schema = User_requestsSchema()
user_requests_schema = User_requestsSchema(many = True)