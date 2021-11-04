from Robots import BattleTech

class Inferno(BattleTech):
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
                 tech_type='INFERNO',
                 armor_slots_num:int=6,
                 weapon_slots_num:int=9,
                 inactiveRounds:int=0,
                 isVisibleNow:int=1,
                 superabilityToUseNum:int=1):
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
                            superabilityToUseNum
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

        Has a 'HELL' UNIQUE ability - needs 33 energy and 10 bullets:

           massive fire attack upon an enemy!
           burns down 35% of remaining energy of enemy tech
           and converts it into an armor and stamina explosive damage in 1 to 1 proportion.
           if during this ability the whole armor of enemy is down
           so the whole remaining damage hits the enemy stamina.
           the total amount of damage also returns to INFERNO stamina in 1 to 1 proportion.
           if INFERNO stamina is full - replenish energy amount in 1 to 1 proportion.
           this ability with 85% probability destroy 1 item of enemy weapon or armor slot
        """

        energyNow = self.get_energy_capacity()
        bulletsNumNow = self.get_bullets_num()
        energyBorder = 33
        bulletsBorder = 10

        if energyNow >= energyBorder and bulletsNumNow >= bulletsBorder:
            print('Unique ability requirements are complied!')
            return True
        else:
            print('Unique ability requirements has not met: ')
            print(f'need energy: {energyBorder}, current energy level: {energyNow}')
            print(f'need bullets: {bulletsBorder}, current bullets num: {bulletsNumNow}')
            return False
