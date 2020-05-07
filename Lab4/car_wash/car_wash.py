#!/usr/bin/env python3
from abc import abstractmethod


class Car:
    def __init__(self):
        self.wash_price = 0

    def get_wash_price(self):
        return self.wash_price

    def add_wash_price(self, price: int):
        self.wash_price += price


class CarWash:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def wash(self, car: Car):
        self._strategy.wash(car)


class Strategy:
    @abstractmethod
    def wash(self, car) -> None:
        pass


class ManualWash(Strategy):
    def __init__(self):
        self.wash_price = 10

    def wash(self, car: Car):
        car.add_wash_price(self.wash_price)
        pass


class AutomaticWash(Strategy):
    def __init__(self):
        self.wash_price = 15

    def wash(self, car: Car):
        car.add_wash_price(self.wash_price)
        pass


def main():
    wash_strategy_a = AutomaticWash()
    wash_strategy_b = ManualWash()
    car1 = Car()
    car2 = Car()
    car3 = Car()

    car_wash = CarWash(wash_strategy_a)
    car_wash.wash(car1)
    car_wash.set_strategy(wash_strategy_b)
    car_wash.wash(car2)
    car_wash.wash(car3)
    car_wash.set_strategy(wash_strategy_a)
    car_wash.wash(car3)

    print(car1.get_wash_price())
    print(car2.get_wash_price())
    print(car3.get_wash_price())


if __name__ == "__main__":
    main()