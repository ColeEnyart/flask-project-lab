from api.models.car import Car

# 'id', 'battery', 'car_name', 'car_name_link', 'efficiency', 'fast_charge', 'price', 'range', 'top_speed', 'acceleration'
car = Car([1, 70, "EV", "https:", 170, 700, 60_000, 400, 160, 5.5])
print('car.__table__: ', car.__table__)
print('car.__dict__: ', car.__dict__)
