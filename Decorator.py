import Beverage


class CondimentDecorator(Beverage):
    def __init__(self, beverage):
        self.beverage = beverage

    def prepare_ingredients(self):
        self.beverage.prepare_ingredients()

    def brew(self):
        self.beverage.brew()

    def add_condiments(self):
        self.beverage.add_condiments()
