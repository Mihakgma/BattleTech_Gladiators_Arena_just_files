from Robots import BattleTech

class Shadow(BattleTech):
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
                 tech_type='SHADOW',
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

        Has a 'HYPERJUMP' UNIQUE ability - needs 23 energy and 199 stamina:

           (a couple of rounds enemy cant hit him with any kind of weapon.
           while SHADOW can use any kind of ordinar weapon - lasers, blasters, machinegun etc...
           during this regenerates 50% of the original - starting energy capacity
           regenerates 70% of lost stamina capacity
           on a last round of it - hits enemy with a shock -
           70% probability of enemy move skipping during 3 next rounds
           and 75% probability to fix 1 item of weapon and 1 item of armor slot of SHADOW)
        """

        energyNow = self.get_energy_capacity()
        staminaNow = self.get_stamina_capacity()
        energyBorder = 23
        staminaBorder = 199

        if energyNow >= energyBorder and staminaNow >= staminaBorder:
            print('Unique ability requirements are complied!')
            return True
        else:
            print('Unique ability requirements has not met: ')
            print(f'need energy: {energyBorder}, current energy level: {energyNow}')
            print(f'need stamina: {staminaBorder}, current stamina level: {staminaNow}')
            return False

    def slowRegenGetBonus(self):
        """"
        If slow regen is activated (this or one of prev round)
        Shadow BT is getting stamina or armor or energy bonuses!

        ATTENTION!
        this bonus cannot be greater then current variable (attribute) baseline value!
        """

        staminaBonus = 7
        armorBonus = 1
        energyBonus = 3
        nickName = self.get_nickname()

        if self.get_stamina_capacity() + staminaBonus <= self.get_baseline_stamina_capacity():
            self.__stamina_capacity += staminaBonus
            print(f'{nickName} успешно восстанавливает {staminaBonus} пунктов стамины!')
        if self.get_armor_volume() + armorBonus <= self.get_baseline_armor_volume():
            self.__armor_volume += armorBonus
            print(f'{nickName} успешно восстанавливает {armorBonus} пунктов брони!')
        if self.get_energy_capacity() + energyBonus <= self.get_baseline_energy_capacity():
            self.__energy_capacity += energyBonus
            print(f'{nickName} успешно восстанавливает {energyBonus} пунктов энергии!')