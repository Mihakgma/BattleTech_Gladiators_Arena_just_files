class Armor():
    """
    Armor types:
    physical - adds usual metal armor effective against machineguns etc
    energetic - adds bonus to energetic shield while using it

    Types of armory:
    1) upgrade the volume of phisical armor (+...% from baseline armor volume)
    2) upgrade the amount of BT overall energy (+...% from baseline energy amount)
    3) boost the speed of BT (+...% from baseline speed)
    """

    # инициализация объекта класса
    def __init__(self,
                 name: str,
                 yearsOld: int,
                 phisicalDefBonus: float,
                 energyBonus: float,
                 speedBonus: float
                 ):
        self.__name = name
        self.__yearsOld = yearsOld
        self.__phisicalDefBonus = phisicalDefBonus
        self.__energyBonus = energyBonus
        self.__speedBonus = speedBonus

    # задать атрибуты
    def setName(self, name):
        self.__name = name

    def setYearsOld(self, yearsOld):
        self.__yearsOld = yearsOld

    def setPhisicalDefBonus(self, phisicalDefBonus):
        self.__phisicalDefBonus = phisicalDefBonus

    def setEnergyBonus(self, energyBonus):
        self.__energyBonus = energyBonus

    def setSpeedBonus(self, speedBonus):
        self.__speedBonus = speedBonus

    # получить атрибуты

    def getName(self):
        return self.__name

    def getYearsOld(self):
        return self.__yearsOld

    def getPhisicalDefBonus(self):
        return self.__phisicalDefBonus

    def getEnergyBonus(self):
        return self.__energyBonus

    def getSpeedBonus(self):
        return self.__speedBonus


