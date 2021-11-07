from Robots import BattleTech

class Mantis(BattleTech):
    # инициализация объекта класса
    def __init__(self,
                 nickname,
                 years_old,
                 armor_volume,
                 stamina_capacity,
                 energy_capacity,
                 missles_num,
                 bullets_num,
                 speed,
                 armor_equipped_lst,
                 weapon_equipped_lst,
                 tech_type='MANTIS',
                 armor_slots_num:int=3,
                 weapon_slots_num:int=5,
                 inactiveRounds:int=0,
                 isVisibleNow:int=1,
                 superabilityToUseNum:int=1,
                 slowRegenStatus:int=0,
                 slowRegenToUseNum:int=1,
                 endedCurrentRound:int=0):
        BattleTech.__init__(self,
                            tech_type,
                            nickname,
                            years_old,
                            armor_volume,
                            stamina_capacity,
                            energy_capacity,
                            missles_num,
                            bullets_num,
                            speed,
                            armor_slots_num,
                            weapon_slots_num,
                            armor_equipped_lst,
                            weapon_equipped_lst,
                            inactiveRounds,
                            isVisibleNow,
                            superabilityToUseNum,
                            slowRegenStatus,
                            slowRegenToUseNum,
                            endedCurrentRound
                            )
        self.__tech_type = tech_type
        self.__nickname = nickname
        self.__years_old = years_old
        self.__armor_volume = armor_volume
        self.__stamina_capacity = round(stamina_capacity, 2)
        self.__energy_capacity = round(energy_capacity, 2)
        self.__missles_num = missles_num
        self.__bullets_num = bullets_num
        self.__speed = speed
        self.__armor_slots_num = armor_slots_num
        self.__weapon_slots_num = weapon_slots_num
        self.__armor_equipped_lst = armor_equipped_lst
        self.__weapon_equipped_lst = weapon_equipped_lst
        self.__inactiveRounds = inactiveRounds
        self.__isVisibleNow = isVisibleNow
        self.__superabilityToUseNum = superabilityToUseNum
        self.__slowRegenStatus = slowRegenStatus
        self.__slowRegenToUseNum = slowRegenToUseNum
        self.__endedCurrentRound = endedCurrentRound

        # проверка на соответсвие длины листов брони и орудий
        if armor_slots_num < len(armor_equipped_lst):
            print('ВНИМАНИЕ!!!')
            print('Длина списка брони больше количества слотов данного типа')


        if weapon_slots_num < len(weapon_equipped_lst):
            print('ВНИМАНИЕ!!!')
            print('Длина списка орудий больше количества слотов данного типа')

    def superAbilityOtherRequirementsAccepted(self):
        """
        reapplied for every type of BattleTech individually!
        If all other requirements (except superabilityToUseNum) are met - returns True.
        This method's result is gonna use as argument for activateUniqueAbility-method
        To let BT use unique ability...

        Has a 'FREEZE' UNIQUE ability - needs 55 energy:


        """

        energyNow = self.get_energy_capacity()
        energyBorder = 55

        if energyNow >= energyBorder:
            print('Unique ability requirements are complied!')
            return True
        else:
            print('Unique ability requirements has not met: ')
            print(f'need energy: {energyBorder}, current energy level: {energyNow}')
            return False