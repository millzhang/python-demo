class Car():
    def __init__(self, brand, price, oil):
        self.brand = brand
        self.price = price
        self.oil = oil

    def showPrice(self):
        print(self.brand + ' valued $' + str(self.price) + '!')

class Bettery():
    def __init__(self, bettery_size=70):
        self.bettery_size = bettery_size

    def get_bettery_size(self):
        print("Bettery Size is " + str(self.bettery_size))


class ElectricCar(Car):
    def __init__(self, brand, price, oil):
        super().__init__(brand, price, oil)
        self.better = Bettery(20) #持有类的属性


myCar = ElectricCar('BMW', 10000, '8L')
myCar.showPrice()
myCar.better.get_bettery_size()