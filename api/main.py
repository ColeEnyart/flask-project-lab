from flask import Flask, request
import psycopg2
from settings import DB_NAME, USER_NAME
from api.models.car import Car

app = Flask(__name__)

app.config.from_mapping(
    DATABASE= DB_NAME,
    USER= USER_NAME
)

@app.route('/cars')
def cars():
    conn = psycopg2.connect(database = app.config['DATABASE'], user = app.config['USER'])
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cars;")
    cars = cursor.fetchall()
    car_objs = [Car(car).__dict__ for car in cars]
    if request.args.get('column') and (request.args.get('more') or request.args.get('less')):
        column = request.args.get('column')
        more = request.args.get('more')
        less = request.args.get('less')
        return Car.filter_column(cursor, column, more, less)
    if request.args.get('column'):
        column = request.args.get('column')
        return Car.select_column(cursor, column)
    return car_objs

@app.route('/cars/<id>')
def show_car(id):
    conn = psycopg2.connect(database = app.config['DATABASE'], user = app.config['USER'])
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cars WHERE id = %s LIMIT 1;", (id,))
    car = cursor.fetchone()
    car_obj = Car(car).__dict__
    return car_obj
