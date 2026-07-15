from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#DEFINE THE MODEL
class cars(db.Model):
    __tablename__= "cars"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    engine_size = db.Column(db.Float, nullable=False)
    fuel_type = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Float, nullable=False)