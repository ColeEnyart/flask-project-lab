class Car():
    __table__ = 'cars'
    columns = ['id', 'battery', 'car_name', 'car_name_link', 'efficiency', 'fast_charge', 'price', 'range', 'top_speed', 'acceleration']

    def __init__(self, values):
        self.__dict__ = dict(zip(self.columns, values))
        
    @classmethod
    def select_column(self, cursor, column):
        if column in self.columns:
            cursor.execute(f"SELECT {column} FROM cars;")
            records = cursor.fetchall()
            return [dict(zip((column,), record)) for record in records]
        return 'NO COLUMN IN TABLE'
    
    @classmethod
    def filter_column(self, cursor, column, start = None, stop = None):
        if column in ['id', 'battery', 'efficiency', 'range', 'top_speed', 'acceleration']:
            self.start_stop(cursor, column, start, stop)
            records = cursor.fetchall()
            return [dict(zip(self.columns, record)) for record in records]
        return 'INVALID COLUMN FOR FILTER BY NUMBER'
    
    def start_stop(cursor, column, start = None, stop = None):
        if start and stop:
            return cursor.execute(f"SELECT * FROM cars WHERE {column} >= {start} AND {column} <= {stop};")
        if start:
            return cursor.execute(f"SELECT * FROM cars WHERE {column} >= {start};")
        if stop:
            return cursor.execute(f"SELECT * FROM cars WHERE {column} <= {stop};")
        