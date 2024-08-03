class House:
    def __init__(self, name, numbers_of_floors):
        # self.new_floor = None  #  !!!
        self.name = name
        self.numbers_of_floors = numbers_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor  # Не пойму зачем Python хочет добавить эту строку в __init__.
        # Обязательно это делать или нет?
        if new_floor < 1 or new_floor > self.numbers_of_floors:
            print(f'В доме "{self.name}" такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(f'Дом "{self.name}", этаж {i}')


house1 = House('ЖК Горский', 18)
house2 = House('Домик в деревне', 2)
house1.go_to(5)
house2.go_to(10)
