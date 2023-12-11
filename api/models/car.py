class Car():
    __table__ = 'cars'
    columns = ['id', 'battery', 'car_name', 'car_name_link', 'efficiency', 'fast_charge', 'price', 'range', 'top_speed', 'acceleration']

    def __init__(self, values):
        self.__dict__ = dict(zip(self.columns, values))
        
    @classmethod
    def select_column(self, cursor, column):
        if column in self.columns:
            cursor.execute(f"SELECT {column} FROM {self.__table__};")
            records = cursor.fetchall()
            return [dict(zip(column, record)) for record in records]
        return 'NO COLUMN IN TABLE'
    
    @classmethod
    def filter_column(self, cursor, column, start = False, stop = False):
        if column in ['id', 'battery', 'efficiency', 'range', 'top_speed', 'acceleration']:
            if start and stop:
                cursor.execute(f"SELECT * FROM cars WHERE {column} >= {start} AND {column} <= {stop};")
            else:
                compare = '>=' if start else '<='
                cursor.execute(f"SELECT * FROM cars WHERE {column} {compare} {start or stop};")
            records = cursor.fetchall()
            return [dict(zip(self.columns, record)) for record in records]
        return 'INVALID COLUMN FOR FILTER BY NUMBER'
        