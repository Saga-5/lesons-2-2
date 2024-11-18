from main import Hero

hero = Hero("Валир", 100)

mage_intro = hero.introduce()
print(mage_intro)

class Mage(Hero):
    def __init__(self, name, health, mana=120):
        super().__init__(name, health)
        self.mana = mana

    def fireball(self):
        if self.mana >= 30:
            self.mana -= 30
            return f"{self.name} использует Огненный шар! Осталось маны: {self.mana}"
        else:
            return f"{self.name} недостаточно маны для Огненного шара."

    def pillar_of_fire(self):
        if self.mana >= 40:
            self.mana -= 40
            return f"{self.name} использует Огненный столб! Осталось маны: {self.mana}"
        else:
            return f"{self.name} недостаточно маны для Огненного столба."

    def fire_prison(self):
        if self.mana >= 20:
            self.mana -= 20
            return f"{self.name} использует Огненную тюрьму! Осталось маны: {self.mana}"
        else:
            return f"{self.name} недостаточно маны для Огненной тюрьмы."

    # Метод для выбора способности
    def use_ability(self, ability_name):
        abilities = {
            "fireball": self.fireball,
            "pillar_of_fire": self.pillar_of_fire,
            "fire_prison": self.fire_prison,
        }
        ability = abilities.get(ability_name.lower())
        if ability:
            return ability()
        else:
            return f"Способность '{ability_name}' не найдена."

mage = Mage("Валир", 100, 120)
print(mage.introduce())

while True:
    user_input = input("Введите название способности (fireball, pillar_of_fire, fire_prison) или 'exit' для выхода: ").strip().lower()

    if user_input == "exit":
        print("Выход из режима выбора способности.")
        break
    else:
        result = mage.use_ability(user_input)
        print(result)
