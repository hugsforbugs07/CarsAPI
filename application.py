from flask import Flask, request, jsonify
from model import db, cars

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db.init_app(app)

@app.route('/')
def home():
    return 'HELLO! THIS IS MY CARS API'

@app.route('/cars')
def get_all_cars():
    vehicles = cars.query.all()

    output = []
    for vehicle in vehicles:
        output.append({
            'id': vehicle.id,
            'make': vehicle.make,
            'model': vehicle.model,
            'year': vehicle.year,
            'engine_size': vehicle.engine_size,
            'fuel_type': vehicle.fuel_type,
            'price': vehicle.price
        })
    return jsonify(output)

@app.route('/cars/<id>', methods=['GET'])
def get_vehicle(id):
    vehicle= cars.query.get_or_404(id)
    return jsonify({
        'id': vehicle.id,
        'make': vehicle.make,
        'model': vehicle.model,
        'year': vehicle.year,
        'engine_size': vehicle.engine_size,
        'fuel_type': vehicle.fuel_type,
        'price': vehicle.price
    })

@app.route('/cars', methods=['POST'])
def add_vehicle():
    data= request.get_json()
    vehicle= cars(
        make=data['make'],
        model=data['model'],
        year=data['year'],
        engine_size=data['engine_size'],
        fuel_type=data['fuel_type'],
        price=data['price']
    )
    db.session.add(vehicle)
    db.session.commit()

    return jsonify({
        "MESSAGE": "ADDED SUCCESSFULLY"
    }), 201


if __name__=="__main__":
    app.run(debug=True)

