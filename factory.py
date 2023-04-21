from abc import abstractmethod
import Beverage


class BeverageFactory():
    @abstractmethod
    def create_beverage(self, **kwargs):
        pass


class MilkTeaFactory(BeverageFactory):
    def __init__(self, storage):
        self.storage = storage

    def create_beverage(self, name, sugar, ice, toppings):
        milk_tea = Beverage.MilkTea(name, sugar, ice)

        return milk_tea
