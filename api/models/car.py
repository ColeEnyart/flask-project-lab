class Car():
    __table__ = 'cars'
    columns = ['id', 'battery', 'car_name', 'car_name_link', 'efficiency', 'fast_charge', 'price', 'range', 'top_speed', 'acceleration']

    def __init__(self, values):
        self.__dict__ = dict(zip(self.columns, values))
        