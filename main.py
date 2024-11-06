class Hero:
    def __init__(self, name, health , ):
        self.name = name
        self.health = health
    def introduce(self):
        return f"Меня звать {self.name}, я великий огненный маг с количеством здоровья: {self.health}"

    def rest(self):
        self.health += 10
        return f"{self.name} отдыхает и восстанавливает здоровье. Новое здоровье: {self.health}"

    def action(self):
        return f"{self.name} выполняет базовое действие.\n"
