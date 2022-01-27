from wiki.pokemon import Pokemon


class Pikatchu(Pokemon):
    no = 25
    clc_name = 'Pikachu'
    def __init__(self, name, lv=5):
        super().__init__(name, lv)
        self.skill = '전기 충격'
        super().increase()
        Pokemon.increase()
       
    def attack(self):
        return '찌릿 찌릿'
    def walk(self):
        return '뚜벅 뚜벅'

class Metamong(Pokemon):
    no = 132

    def __init__(self, name, lv=5):
        super().__init__(name, lv)
        self.skill = '변신'
        print(super())
    def eat(self):
        return '냠냠'

class Child(Pikatchu, Metamong):
    def __init__(self, name, lv=5):
        super().__init__(name, lv)
        print(super())
    pass

# c = Child('피카츄?')
# print(c.no, c.eat(), c.attack())


pika = Pikatchu('피카츄')
# meta = Metamong('메타몽')


# print(meta.no, meta.attack())

print("피카츄 인구: ", Pikatchu.population, "  포켓몬 인구: ", Pokemon.population)