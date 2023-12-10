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
    def filter_column(self, cursor, column, more = False, less = False):
        if column in ['id', 'battery', 'efficiency', 'range', 'top_speed', 'acceleration']:
            if more and less:
                cursor.execute(f"SELECT * FROM cars WHERE {column} > {more} AND {column} < {less};")
            else:
                compare = '>' if more else '<'
                cursor.execute(f"SELECT * FROM cars WHERE {column} {compare} {more or less};")
            records = cursor.fetchall()
            return [dict(zip(self.columns, record)) for record in records]
        return 'INVALID COLUMN FOR FILTER BY NUMBER'
        