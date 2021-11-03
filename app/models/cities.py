import datetime
from app import db, ma


class Cities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_request_id = db.Column(db.Integer, db.ForeignKey('user_requests.id'), nullable=False)
    city = db.Column(db.Integer)
    temp = db.Column(db.Float)
    humidity = db.Column(db.Float)
    time  = db.Column(db.DateTime)

    def __init__(self, user_request_id: int, city: int, temp: float, humidity: float, time: datetime) -> None:
        self.user_request_id: int  = user_request_id
        self.city: int = city
        self.temp: float  = temp
        self.humidity: float = humidity
        self.time: datetime = time
    

class CitiesSchema(ma.Schema):
    class Meta:
        fields = ('id','user_request_id', 'city', 'temp', 'humidity')


city_schema = CitiesSchema()
cities_schema = CitiesSchema(many=True)
