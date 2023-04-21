class Storage:
    def __init__(self):
        self.stock = {
            "珍珠": 100,
            "布丁": 50,
            "椰果": 30,
            "仙草": 20,
            "红茶": 200,
            "绿茶": 200,
            "乌龙茶": 200,
            "芒果": 50,
            "草莓": 50,
            "蜜桃": 50,
            "咖啡豆": 100,
            "鲜奶油": 50,
            "草莓酱": 50,
            "巧克力酱": 50,
            "香草冰淇淋": 30,
            "巧克力冰淇淋": 30,
            "草莓冰淇淋": 30
        }

    def get_ingredient(self, ingredient_name, num):
        if ingredient_name not in self.stock:
            raise ValueError(f"{ingredient_name} 不是有效的原材料")
        if self.stock[ingredient_name] <= num:
            raise ValueError(f"{ingredient_name} 原料不足")
        self.stock[ingredient_name] -= num
        return 1


class Material:
    def __init__(self, name, num):
        if Storage.get_ingredient(name, num) == 1:
            self.name = name
            self.num = num
