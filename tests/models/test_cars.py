import pytest
import psycopg2
import simplejson as json
from settings import DB_NAME, USER_NAME
from api.models.car import Car

def test_init_car():
    car = Car([1, 70, "EV", "https:", 170, 700, 60_000, 400, 160, 5.5])
    assert car.__dict__ == {'id': 1, 
                            'battery': 70, 
                            'car_name': 'EV', 
                            'car_name_link': 'https:', 
                            'efficiency': 170, 
                            'fast_charge': 700, 
                            'price': 60000, 
                            'range': 400, 
                            'top_speed': 160, 
                            'acceleration': 5.5}
    
@pytest.fixture()
def psql_conn():
    conn = psycopg2.connect(database = DB_NAME, user = USER_NAME)
    return conn.cursor()

def test_select_column_in_table(psql_conn):
    car = Car.select_column(psql_conn, 'baery')
    assert car == 'NO COLUMN IN TABLE'
        
def test_select_column(psql_conn):
    car = Car.select_column(psql_conn, 'battery')
    assert json.dumps(car[:3]) == json.dumps([{"battery": 75}, {"battery": 57.5}, {"battery": 60.5}])

def test_filter_column_is_filterable(psql_conn):
    car = Car.splice_column(psql_conn, 'baery')
    assert car == 'INVALID COLUMN FOR SPLICING'
    
def test_filter_column_start_and_stop(psql_conn):
    car = Car.splice_column(psql_conn, 'id', 3, 4)
    assert json.dumps(car) == json.dumps([{
            "id": 3,
            "battery": 60.5,
            "car_name": "BYD ATTO 3",
            "car_name_link": "https://ev-database.org/car/1782/BYD-ATTO-3",
            "efficiency": 183,
            "fast_charge": "370",
            "price": "44625",
            "range": 330,
            "top_speed": 160,
            "acceleration": 7.3}, 
            {
            "id": 4,
            "battery": 61.7,
            "car_name": "MG MG4 Electric 64 kWh",
            "car_name_link": "https://ev-database.org/car/1708/MG-MG4-Electric-64-kWh",
            "efficiency": 171,
            "fast_charge": "630",
            "price": "39990",
            "range": 360,
            "top_speed": 160,
            "acceleration": 7.9}])   
    
def test_filter_column_start(psql_conn):
    car = Car.splice_column(psql_conn, 'id', 359)
    assert json.dumps(car) == json.dumps([{
            "id": 359,
            "battery": 68,
            "car_name": "Opel Zafira-e Life M 75 kWh",
            "car_name_link": "https://ev-database.org/car/1348/Opel-Zafira-e-Life-M-75-kWh",
            "efficiency": 257,
            "fast_charge": "290",
            "price": "69250",
            "range": 265,
            "top_speed": 130,
            "acceleration": 13.3},
            {
            "id": 360,
            "battery": 46.3,
            "car_name": "Fiat E-Ulysse L3 50 kWh",
            "car_name_link": "https://ev-database.org/car/1723/Fiat-E-Ulysse-L3-50-kWh",
            "efficiency": 257,
            "fast_charge": "290",
            "price": "56990",
            "range": 180,
            "top_speed": 130,
            "acceleration": 12.1}])

def test_filter_column_stop(psql_conn):
    car = Car.splice_column(psql_conn, 'id', stop=2)
    assert json.dumps(car) == json.dumps([{
            "id": 1,
            "battery": 75,
            "car_name": "Tesla Model Y Long Range Dual Motor",
            "car_name_link": "https://ev-database.org/car/1619/Tesla-Model-Y-Long-Range-Dual-Motor",
            "efficiency": 172,
            "fast_charge": "670",
            "price": "59017",
            "range": 435,
            "top_speed": 217,
            "acceleration": 5},
            {
            "id": 2,
            "battery": 57.5,
            "car_name": "Tesla Model 3",
            "car_name_link": "https://ev-database.org/car/1991/Tesla-Model-3",
            "efficiency": 137,
            "fast_charge": "700",
            "price": "46220",
            "range": 420,
            "top_speed": 201,
            "acceleration": 6.1}])
