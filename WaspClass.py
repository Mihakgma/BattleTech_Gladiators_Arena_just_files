from Robots import BattleTech

class Wasp(BattleTech):
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
                 tech_type='WASP',
                 armor_slots_num:int=2,
                 weapon_slots_num:int=3,
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

    def uniqueAbilityOtherRequirementsAccepted(self):
        """
        reapplied for every type of BattleTech individually!
        If all other requirements (except superabilityToUseNum) are met - returns True.
        This method's result is gonna use as argument for activateUniqueAbility-method
        To let BT use unique ability...

        Has a 'POISONOUS STING' UNIQUE ability - needs 39 energy & 33 bullets:
           (
           add poison to machinegun bullets for the rest of the battle.
           poison makes additional damage (27% of the basic bullets damage)
           which ignores armor, phisical or even energy shields
           )
        """

        energyNow = self.get_energy_capacity()
        bulletsNumNow = self.get_bullets_num()
        energyBorder = 39
        bulletsBorder = 33

        if energyNow >= energyBorder and bulletsNumNow >= bulletsBorder:
            print('Unique ability requirements are complied!')
            return True
        else:
            print('Unique ability requirements has not met: ')
            print(f'need energy: {energyBorder}, current energy level: {energyNow}')
            print(f'need bullets: {bulletsBorder}, current bullets num: {bulletsNumNow}')
            return False