import pandas as pd

from application import app
from model import db,cars
 
df= pd.read_csv("CARS_DATA.csv")

df= df.where(pd.notnull(df), None)

with app.app_context():

    db.drop_all()
    db.create_all()

    for _, row in df.iterrows():
        vehicle= cars(
            make=row['make'],
            model=row['model'],
            year=row['year'],
            engine_size=row['engine_size'],
            fuel_type=row['fuel_type'],
            price=row['price']
        )

        db.session.add(vehicle)

    db.session.commit()

print("DATA IMPORTED SUCCESSFULLY!!!!")

