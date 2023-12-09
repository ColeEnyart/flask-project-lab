from flask import Flask, jsonify
import psycopg2
from settings import DB_NAME, USER_NAME

app = Flask(__name__)

app.config.from_mapping(
    DATABASE= DB_NAME,
    USER= USER_NAME
)

@app.route('/cars')
def venues():
    conn = psycopg2.connect(database = app.config['DATABASE'], user = app.config['USER'])
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cars;')
    cars = cursor.fetchall()
    return jsonify(cars)

@app.route('/cars/<id>')
def show_venue(id):
    conn = psycopg2.connect(database = app.config['DATABASE'], user = app.config['USER'])
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cars WHERE id = %s LIMIT 1;", id)
    car = cursor.fetchone()
    return jsonify(car)
