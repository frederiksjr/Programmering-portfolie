class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print(f"{self.make} {self.model} is starting.")

    def stop(self):
        print(f"{self.make} {self.model} is stopping.")

    def drive(self):
        print(f"{self.make} {self.model} is being driven.")

    def honk(self):
        print("Beep beep!")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_level = 100

    def drive(self):
        if self.battery_level > 0:
            self.battery_level -= 10
            print(
                f"{self.make} {self.model} is being driven. Battery level: {self.battery_level}%")
        else:
            print(f"{self.make} {self.model} is out of battery.")

    def charge(self):
        self.battery_level = 100
        print(
            f"{self.make} {self.model} is charging. Battery level: {self.battery_level}%")


class GasCar(Car):
    def __init__(self, make, model, year, gas_level):
        super().__init__(make, model, year)
        self.gas_level = gas_level

    def drive(self):
        if self.gas_level > 0:
            self.gas_level -= 10
            print(
                f"{self.make} {self.model} is being driven. Gas level: {self.gas_level}%")
        else:
            print(f"{self.make} {self.model} is out of gas.")

    def refill(self):
        self.gas_level = 100
        print(f"{self.make} {self.model} is refilled. Gas level: {self.gas_level}%")


tesla = ElectricCar("Tesla", "Model S", 2020)
audi = GasCar("Audi", "A8", 2019, 90)

tesla.start()
tesla.drive()
tesla.stop()
tesla.charge()

audi.start()
audi.drive()
audi.stop()
audi.refill()
