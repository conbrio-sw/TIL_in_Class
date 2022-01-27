class Pokemon:
    population = 0
    clc_name = 'Pokemon'
    def __init__(self, name, lv = 0):
        self.name = name
        self.lv = lv + 1
        self.skill = '몸통 박치기'
        # Pokemon.population += 1
        self.increase()
        
    def attack(self):
        return self.skill
        pass
    @classmethod
    def increase(cls):
        cls.population += 1
        pass
    pass