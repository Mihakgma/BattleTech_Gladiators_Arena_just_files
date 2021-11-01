class Weapon():
    """
    Damage points - damage made by the weapon per round
    Damage type:
    1) phisical (machineguns etc);
    2) explosive (rocket launchers, cannons etc);
    3) thermal (spitfires etc);
    4) energetic (blasters, lazers etc)...
    """

    # инициализация объекта класса
    def __init__(self,
                 damage_type,
                 name,
                 years_old,
                 endurance_volume,
                 damage_points
                 ):
        self.__damage_type = damage_type
        self.__name = name
        self.__years_old = years_old
        self.__endurance_volume = endurance_volume
        self.__damage_points = damage_points

    # задать атрибуты
    def set_damage_type(self, damage_type):
        self.__damage_type = damage_type

    def set_name(self, name):
        self.__name = name

    def set_years_old(self, years_old):
        self.__years_old = years_old

    def set_endurance_volume(self, endurance_volume):
        self.__endurance_volume = endurance_volume

    def set_damage_points(self, damage_points):
        self.__damage_points = damage_points

    # получить атрибуты
    def get_damage_type(self):
        return self.__damage_type

    def get_name(self):
        return self.__name

    def get_years_old(self):
        return self.__years_old

    def get_endurance_volume(self):
        return self.__endurance_volume

    def get_damage_points(self):
        return self.__damage_points

    def getAllAttributes(self):
        print(f'Тип урона: <{self.get_damage_type()}>')
        print(f'Наименование орудия: {self.get_name()}')
        print(f'Возраст(лет): {self.get_years_old()}')
        print(f'Прочность (ед.): {self.get_endurance_volume()}')
        print(f'Наносимый урон(пунктов): {self.get_damage_points()}')
