class Car:
    car_name="mdc"

    def __init__(self,agv,price):
        self.agv=agv
        self.price=price
    def display_carname(self) :
        print(f'car is {self.car_name} with average {self.agv} with good price {self.price}')
    def buy_car(self,str):
        print(f'you have bought {self.car_name} with average {self.agv} with')
class Maruty(Car):
    def __init__(self, agv, price):
        super().__init__(agv, price)  
class Lambo(Car):
    def __init__(self, agv, price):
        super().__init__(agv, price)  
class Marsadisg(Car):
    def __init__(self, agv, price):
        super().__init__(agv, price)  




m=Maruty(123,123456)
m.car_name="Marity"
m.display_carname()
m.buy_car("Marity")
l=Lambo(230,909090090)
l.car_name="Lambo"
l.display_carname()
l.buy_car("Lambo")
md=Marsadisg(229,898989)
md.car_name="Marsadisg"
md.display_carname()
md.buy_car("Marsadisg")
