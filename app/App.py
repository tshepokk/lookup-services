from flask import Flask, request
from geopy import Nominatim
from geopy.point import Point

geolocator = Nominatim(user_agent="myApp")
app = Flask(__name__)

@app.route('/lat_lng')
def lat_lng():
    lat = request.args['lat']
    lng = request.args['lng']

    location = geolocator.reverse(f'{lat}, {lng}')

    print(type(location))
   
    return location.raw

@app.route('/address')

def address():
    return 'lat and lng'


if __name__ == '__main__':
    app.run(debug= True)