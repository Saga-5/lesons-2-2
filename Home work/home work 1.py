
class Persson:
    def __init__(self, name, age , city):
        self.name = name
        self.age = age
        self.city = city

    def introduse(self):
        print("Меня зовут", self.name ,"мне" ,self.age,"лет, я живу в" ,self.city)

    def is_adult(self):
        if self.age >= 18:
            print(True)
        else:
            print(False)

    def __str__(self):
        return f'Имя: {self.name}, возраст: {self.age}, город: {self.city}'

Sultan=Persson(name="Султан", age=19, city="Бишкек" )
Argen=Persson(name="Арген", age=17 , city='Корея')
Dayana=Persson(name="Даяна" , age=18, city="Германия")
Dima=Persson(name="Дима", age=16 , city="Россия")

Sultan.introduse()
Sultan.is_adult()

Argen.introduse()
Argen.is_adult()

Dayana.introduse()
Dayana.is_adult()

print(Dima)