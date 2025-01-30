class Car:
    car_name='kkgkjbjghfdh'# class Variable who share all the instance

    def __init__(self,car_name):
        self.car_name=car_name # instance variable

car=Car("new car")
print(car.car_name)  # prints: new car
        