class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class MilkTea(Beverage):
    def __init__(self, name, price, sweetness, ice, toppings):
        super().__init__(name, price)
        self.sweetness = sweetness
        self.ice = ice
        self.toppings = toppings


class Tea(Beverage):
    def __init__(self, name, price, temperature, steep_time):
        super().__init__(name, price)
        self.temperature = temperature
        self.steep_time = steep_time


class FruitTea(Beverage):
    def __init__(self, name, price, sweetness, ice, fruit):
        super().__init__(name, price)
        self.sweetness = sweetness
        self.ice = ice
        self.fruit = fruit


class Coffee(Beverage):
    def __init__(self, name, price, size, strength, milk):
        super().__init__(name, price)
        self.size = size
        self.strength = strength
        self.milk = milk


class Juice(Beverage):
    def __init__(self, name, price, fruit):
        super().__init__(name, price)
        self.fruit = fruit


class IceCream(Beverage):
    def __init__(self, name, price, flavor, topping):
        super().__init__(name, price)
        self.flavor = flavor
        self.topping = topping


milktea_menu = {
    "原味奶茶": MilkTea("原味奶茶", 10.0, "正常糖", "正常冰", []),
    "珍珠奶茶": MilkTea("珍珠奶茶", 12.0, "正常糖", "正常冰", ["珍珠"]),
    # 其他品种...
}

tea_menu = {
    "铁观音": Tea("铁观音", 8.0, "热", 3),
    "龙井": Tea("龙井", 8.0, "热", 2),
    # 其他品种...
}

fruittea_menu = {
    "芒果冰沙": FruitTea("芒果冰沙", 15.0, "半糖", "去冰", ["芒果"]),
    "西瓜汁": FruitTea("西瓜汁", 12.0, "全糖", "多冰", ["西瓜"]),
    # 其他品种...
}

coffee_menu = {
    "拿铁": Coffee("拿铁", 15.0, "中杯", "中度", "牛奶"),
    "美式": Coffee("美式", 12.0, "小杯", "中度", ""),
}
