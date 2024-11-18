from abc import ABC

class Room(ABC):
    def __init__(self, features, price):
        self._features = features
        self.__price = price

    def get_price(self):
        return self.__price

    def get_features(self):
        return self._features



class StandardRoom(Room):
    pass

class LuxuryRoom(Room):
    pass

class FamilyRoom(Room):
    pass


class WiFiService:
    def get_wifi_description(self):
        return "Высокоскоростной Wi-Fi"

class BreakfastService:
    def get_breakfast_description(self):
        return "Бесплатный завтрак"


class LuxuryRoomWithServices(LuxuryRoom, WiFiService, BreakfastService):
    def get_features(self):
        features = self._features.copy()
        features.append(self.get_wifi_description())
        features.append(self.get_breakfast_description())
        return features


class FamilyRoomWithServices(FamilyRoom, WiFiService):
    def get_features(self):
        features = self._features.copy()
        features.append(self.get_wifi_description())
        return features


standard_room = StandardRoom(["Односпальная кровать", "Письменный стол"], 100)
luxury_room = LuxuryRoomWithServices(["Кровать King-size", "Джакузи"], 300)
family_room = FamilyRoomWithServices(["Двуспальная кровать", "Детская кроватка"], 200)

print("Обычная комната:")
print("Цена:", standard_room.get_price())
print("Удобства:", standard_room.get_features())

print("\nЛюкс комната с услугами:")
print("Цена:", luxury_room.get_price())
print("Удобства:", luxury_room.get_features())

print("\nСемейная комната с услугами:")
print("Цена:", family_room.get_price())
print("Удобства:", family_room.get_features())
