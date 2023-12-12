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
def psql_conn():
    conn = psycopg2.connect(database = app.config['DATABASE'], user = app.config['USER'])
    cursor = conn.cursor()
    return cars_view(cursor)

def cars_view(cursor):
    all_args = request.args.to_dict()
    if all_args.get('column') and (all_args.get('start') or all_args.get('stop')):
        return Car.splice_column(cursor, all_args.get('column'), all_args.get('start'), all_args.get('stop'))
    if all_args.get('column'):
        return Car.select_column(cursor, all_args.get('column'))
    return cars_no_query(cursor)

def cars_no_query(cursor):
    cursor.execute("SELECT * FROM cars;")
    cars = cursor.fetchall()
    return [Car(car).__dict__ for car in cars]

@app.route('/cars/<id>')
def show_car(id):
    conn = psycopg2.connect(database = app.config['DATABASE'], user = app.config['USER'])
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cars WHERE id = %s LIMIT 1;", (id,))
    car = cursor.fetchone()
    return Car(car).__dict__
