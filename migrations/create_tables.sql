DROP TABLE IF EXISTS cars;

CREATE TABLE IF NOT EXISTS cars (
    id serial PRIMARY KEY,
    battery DECIMAL,
    car_name VARCHAR(255) NOT NULL,
    car_name_link VARCHAR(255) NOT NULL,
    efficiency INTEGER,
    fast_charge VARCHAR(255) NOT NULL,
    price VARCHAR(255) NOT NULL,
    range INTEGER,
    top_speed INTEGER,
    acceleration DECIMAL
);

-- psql -d ev_cars -U postgres -f migrations/create_tables.sql
/*
psql -d ev_cars -U postgres -c "\copy cars
(battery, car_name, car_name_link, efficiency, fast_charge, price, range, top_speed, acceleration) 
FROM 'EV_cars.csv' DELIMITER ',' CSV HEADER;"
*/
-- psql -d ev_cars -U postgres -c 'SELECT * FROM cars LIMIT 5;'
