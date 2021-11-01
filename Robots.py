from Weaponry import *
from os import urandom as os_urandom


class BattleTech():

    # инициализация объекта класса
    def __init__(self,
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
                 weapon_equipped_lst
                 ):
        """
        TECHTYPES:
        1) GLADIATOR - has powerful weapons heavy-armoured (missles & machineguns) with but
           tiny energy capacity, very slow, with huge ammo capacity (missles, bullets etc)
           and big stamina.
           Missles attacks gives 7.5% probability to destroy any kind of enemy
           slot item (armor or weapon) only when enemy doesn't use energy shield!
           Slow regeneration of stamina is available during whole the battle
           (need to waste a round to turn it on (only once per battle) -
           insusceptibility to any kind of enemy attack during this round).

           Has a 'GENOCIDE' UNIQUE ability - needs 333 energy and 15 missles:

           (mass missles single discharge with a huge explosive damage
           enemy which underwent this ability slows down by 59% during 3 next rounds.
           while this regenerates 35% of armor lost during current battle
           and 75% probability to fix 1 item of weapon and 1 item of armor slot)


        2) SHADOW - weak explosive weaponry (missles) and metal armour compensates with a huge
           amount of energy capacity as well as fast blasters and precise lazers. Very fast.
           Has a fast machineguns with high percent (25%) of critical strike hits upon an armor.
           Lazer and blaster attacks gives 5.5% probability to destroy any kind of enemy
           slot item (armor or weapon) despite of enemy using or not energy shield!
           Slow regeneration of energy is available during whole the battle
           (need to waste a round to turn it on (only once per battle) -
           insusceptibility to any kind of enemy attack during this round).

           Has a 'HYPERJUMP' UNIQUE ability - needs 555 energy:

           (a couple of rounds enemy cant hit him with any kind of weapon.
           while SHADOW can use any kind of ordinar weapon - lasers, blasters, machinegun etc...
           during this regenerates 50% of the original - starting energy capacity
           regenerates 70% of lost stamina capacity
           on a last round of it - hits enemy with a shock -
           70% probability of enemy move skipping during 3 next rounds
           and 75% probability to fix 1 item of weapon and 1 item of armor slot of SHADOW)


        3) INFERNO - medium missles force, weak lazers but has machinegun with medium damage.
           Has a spitfire which ignores metal armor (but quickly destroy it) and penetrates
           on 45% through any kind of energy shield.
           Fire attacks gives 3.5% probability to destroy any kind of enemy
           slot item (armor or weapon) despite of enemy using or not energy shield!
           Slow regeneration of stamina is available during whole the battle
           (need to waste a round to turn it on (only once per battle) -
           insusceptibility to any kind of enemy attack during this round).
           Slow regeneration of energy is available during whole the battle
           (need to waste a round to turn it on (only once per battle) -
           insusceptibility to any kind of enemy attack during this round).

           Has a 'HELL' UNIQUE ability - needs 432 energy:
           (
           massive fire attack upon an enemy!
           burns down 35% of remaining energy of enemy tech
           and converts it into an armor and stamina explosive damage in 1 to 1 proportion.
           if during this ability the whole armor of enemy is down
           so the whole remaining damage hits the enemy stamina.
           the total amount of damage also returns to INFERNO stamina in 1 to 1 proportion.
           if INFERNO stamina is full - replenish energy amount in 1 to 1 proportion.
           this ability with 85% probability destroy 1 item of enemy weapon or armor slot
           )
           ...
           Length of armor and weapon lists cant be more than
           armor_slots_num and weapon_slots_num accordingly.
           If Len of one of the lists is bigger of the slots number or < 1 so the warning message
           pops before the initialization of the current class object.
           And the initialization process cant be performed!

        """
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

        # проверка на соответсвие длины листов брони и орудий
        if armor_slots_num < len(armor_equipped_lst):
            print('ВНИМАНИЕ!!!')
            print('Длина списка брони больше количества слотов данного типа')
            # kill_self()

        if weapon_slots_num < len(weapon_equipped_lst):
            print('ВНИМАНИЕ!!!')
            print('Длина списка орудий больше количества слотов данного типа')
            # kill_self()

    # задать атрибуты
    def set_nickname(self, nickname):
        self.__nickname = nickname

    def set_tech_type(self, tech_type):
        self.__tech_type = tech_type

    def set_years_old(self, years_old):
        self.__years_old = years_old

    def set_armor_volume(self, armor_volume):
        self.__armor_volume = armor_volume

    def set_stamina_capacity(self, stamina_capacity):
        self.__stamina_capacity = stamina_capacity

    def set_energy_capacity(self, energy_capacity):
        self.__energy_capacity = energy_capacity

    def set_missles_num(self, missles_num):
        self.__missles_num = missles_num

    def set_bullets_num(self, bullets_num):
        self.__bullets_num = bullets_num

    def set_speed(self, speed):
        self.__speed = speed

    def set_armor_slots_num(self, armor_slots_num):
        self.__armor_slots_num = armor_slots_num

    def set_weapon_slots_num(self, weapon_slots_num):
        self.__weapon_slots_num = weapon_slots_num

    def set_armor_equipped_lst(self, armor_equipped_lst):
        self.__armor_equipped_lst = armor_equipped_lst

    def set_weapon_equipped_lst(self, weapon_equipped_lst):
        self.__weapon_equipped_lst = weapon_equipped_lst

    # получить атрибуты
    def get_nickname(self):
        return self.__nickname

    def get_tech_type(self):
        return self.__tech_type

    def get_years_old(self):
        return self.__years_old

    def get_armor_volume(self):
        return round(self.__armor_volume, 2)

    def get_stamina_capacity(self):
        return round(self.__stamina_capacity, 2)

    def get_energy_capacity(self):
        return self.__energy_capacity

    def get_missles_num(self):
        return self.__missles_num

    def get_bullets_num(self):
        return self.__bullets_num

    def get_speed(self):
        return self.__speed

    def get_armor_slots_num(self):
        return self.__armor_slots_num

    def get_weapon_slots_num(self):
        return self.__weapon_slots_num

    def get_armor_equipped_lst(self):
        return self.__armor_equipped_lst

    def get_weapon_equipped_lst(self):
        return self.__weapon_equipped_lst

    # print all atributes by doing 1 method
    def showAllAttrValues(self):
        """
        show eg print values
        of all attributes of the current
        BattleTech one
        """
        print('Ник: ', self.get_nickname())
        print('Выбранный тип BattleTech: ', self.get_tech_type())
        print('Возраст: ', self.get_years_old(), 'лет')
        print('Объем брони: ', self.get_armor_volume(), 'пунктов')
        print('Стамина: ', self.get_stamina_capacity(), 'пунктов')
        print('Энергия: ', self.get_energy_capacity(), 'пунктов')
        print('Боезапас ракет: ', self.get_missles_num(), 'штук')
        print('Боезапас патронов: ', self.get_bullets_num(), 'штук')
        print('Скорость: ', self.get_speed(), 'км/ч')
        print('Слотов брони BattleTech: ', self.get_armor_slots_num(), 'штук')
        print('Слотов оружия BattleTech: ', self.get_weapon_slots_num(), 'штук')
        print(f'Экипирована броня: {self.get_armor_equipped_lst()}')
        print(f'Экипировано оружие: {[i.get_name() for i in self.get_weapon_equipped_lst()]}')

    # БОЕВКА
    # МЕТОДЫ ЗАЩИТЫ
    def move(self):
        """
        Передвигает робота (уклонение)
        эффективно от ракетного залпа
        """
        currentSpeed = self.get_speed()
        currentNickname = self.get_nickname()
        if currentSpeed > 0:
            #print(f'{currentNickname} применяет уклонение на скорости {currentSpeed}')
            return True, 'move'
        else:
            print(f'{currentNickname} не может стронуться с места!')
            print('Reason: Not enough speed!')
            return False, 'move'


    def activateEnergyShield(self):
        """
        Активизирует энергетический щит.
        Эффективен против лазеров (?) и Огнеметов.
        может быть применен только если у BattleTech-а осталась энергия
        """
        if self.get_energy_capacity() > 0:
            #print(f'{self.get_nickname()} активирует энергетический щит!')
            return True, 'energy shield'
        else:
            print(f'{self.get_nickname()} не может активировать энергетический щит!')
            print('Reason: Not enough energy!')
            return False, 'energy shield'

    def activatePhisicalShield(self):
        """
        Активизирует щит, эффективный от физических атак,
        может быть применен только если у BattleTech-а осталась броня
        :return:
        """
        if self.get_armor_volume() > 0:
            #print(f'{self.get_nickname()} активирует физический щит!')
            return True, 'phisical shield'
        else:
            print(f'{self.get_nickname()} не может активировать физический щит!')
            print('Reason: Not enough armor volume!')
            return False, 'phisical shield'

    # МЕТОДЫ АТАКИ
    def use_weapon_by_lst_index(self, weapon_equipped_index: int):
        """
        Использует выбранное оружие для
        нанесения урона противнику
        возвращает тип и объем урона в виде tuple
        """
        chosen_weapon = self.get_weapon_equipped_lst()[weapon_equipped_index]
        damageType = chosen_weapon.get_damage_type()
        damage = chosen_weapon.get_damage_points()

        phisicalSpendAmmo = 3
        explosiveSpendAmmo = 1
        thermalSpendAmmo = 1
        energeticSpendAmmo = 1
        fireSuccessfulFlag = False

        def fireSuccessful(
                weaponDidntFail=1,
                currNickname=self.get_nickname(),
                currWeapon=chosen_weapon.get_name(),
                damage=damage,
                damageType=damageType
        ):
            if weaponDidntFail:
                print(f'{currNickname} использует {currWeapon}!')
                print(f'И собирается нанести {damage} пунктов <{damageType}> урона!')

                return True
            else:
                print(f'{currNickname} пытается использовать {currWeapon}!')
                print('Орудие не сработало!')
                return False

        damageAmmoTypesDict = {
            'phisical': [self.get_bullets_num(), 'шт.'],
            'explosive': [self.get_missles_num(), 'ракет'],
            'thermal': [self.get_energy_capacity(), 'пунктов энергии'],
            'energetic': [self.get_energy_capacity(), 'пунктов энергии']
        }

        currWeaponFailProbability = round(chosen_weapon.get_years_old() * 0.007, 3)
        randomProbability = round(int.from_bytes(os_urandom(8), byteorder="big") / ((1 << 64) - 1), 5)
        print(f'Weapon fail probs: {currWeaponFailProbability} '
              f'Random probs got now: {randomProbability}')

        # Оружие "закусило" или не сработало
        if randomProbability <= currWeaponFailProbability:
            damage = 0  # обнуляем наносимый урон
            fireSuccessfulFlag = fireSuccessful(weaponDidntFail=0)
            return '', 0

        # в зависимости от типа урона, который наносит орудие убавляется определенный боезапас

        elif damageType == 'phisical' and self.get_bullets_num() - phisicalSpendAmmo >= 0:
            self.__bullets_num -= phisicalSpendAmmo
            fireSuccessfulFlag = fireSuccessful()
        elif damageType == 'explosive' and self.get_missles_num() - explosiveSpendAmmo >= 0:
            self.__missles_num -= explosiveSpendAmmo
            fireSuccessfulFlag = fireSuccessful()
        elif damageType == 'thermal' and self.get_energy_capacity() - thermalSpendAmmo >= 0:
            self.__energy_capacity -= thermalSpendAmmo
            fireSuccessfulFlag = fireSuccessful()
        elif damageType == 'energetic' and self.get_energy_capacity() - energeticSpendAmmo >= 0:
            self.__energy_capacity -= energeticSpendAmmo
            fireSuccessfulFlag = fireSuccessful()

        else:
            print(f'{self.get_nickname()} не получается использовать {chosen_weapon.get_name()}!')
            print(
                f'Боезапас для <{damageType}> типа орудий исчерпан и составляет {damageAmmoTypesDict[damageType][0]} {damageAmmoTypesDict[damageType][1]}')
            damage = 0  # обнуляем наносимый урон
            return '', 0

        if fireSuccessfulFlag:
            return damageType, damage

    # Unique abilities methods
    def activateUniqueAbility(self):
        pass

    # получение урона
    # Stamina
    def getStaminaDamage(self, damageGot):
        """
        получение урона здоровью по количеству damageGot
        """
        currentNickName = self.get_nickname()
        currentBTStaminaCapacity = self.get_stamina_capacity()
        if currentBTStaminaCapacity > 0:
            self.__stamina_capacity -= damageGot
            print(f'Стамина {currentNickName} уменьшилась на {damageGot} пунктов')
            if self.get_stamina_capacity() < 0:
                # стамина не может быть ниже нуля!!!
                self.__stamina_capacity = 0
                print(f'Стамина {currentNickName} - ниже 0 пунктов. Ему пришел каюк! :-(')
                self.kill_self()
        if currentBTStaminaCapacity < 0:
            print(f'{currentNickName} уже выведен из боя!')

    # Armor
    def getArmorDamage(self, damageGot):
        """
        получение броней урона
        """
        armorMinusDamage = self.get_armor_volume() - damageGot

        if self.get_armor_volume() < 1:
            self.getStaminaDamage(damageGot)

        elif self.get_armor_volume() > 0 and armorMinusDamage >= 0:
            # armorBefore = self.get_armor_volume()
            self.__armor_volume -= damageGot
            print(f'Броня {self.get_nickname()} уменьшилась на {damageGot} пунктов')
            if self.get_armor_volume() == 0:
                print(f'{self.get_nickname()} остался без брони!')

        elif self.get_armor_volume() > 0 and armorMinusDamage < 0:
            self.__armor_volume = 0
            self.getStaminaDamage(armorMinusDamage * -1)

    def kill_self(self):
        """
        Удалить объект класса (?)
        поражение данного BattleTech-а
        """
        # del self
        print('BOOM!')


testBT1 = BattleTech(
    tech_type='GLADIATOR',
    nickname='Stix',
    years_old=3,
    armor_volume=700,
    stamina_capacity=599,
    energy_capacity=35,
    missles_num=25,
    bullets_num=40,
    speed=5,
    armor_slots_num=3,
    weapon_slots_num=5,
    armor_equipped_lst=['', '', ''],
    weapon_equipped_lst=[machinegun1, cannon1, lazer2, rocketLauncher3]
)

testBT2 = BattleTech(
    tech_type='GLADIATOR',
    nickname='Zeus',
    years_old=55,
    armor_volume=900,
    stamina_capacity=499,
    energy_capacity=30,
    missles_num=50,
    bullets_num=39,
    speed=15,
    armor_slots_num=5,
    weapon_slots_num=5,
    armor_equipped_lst=['', '', ''],
    weapon_equipped_lst=[machinegun1, cannon1, lazer1, rocketLauncher2]
)

testBT3 = BattleTech(
    tech_type='INFERNO',
    nickname='Sparkie',
    years_old=33,
    armor_volume=500,
    stamina_capacity=499,
    energy_capacity=70,
    missles_num=10,
    bullets_num=30,
    speed=45,
    armor_slots_num=3,
    weapon_slots_num=4,
    armor_equipped_lst=['', '', ''],
    weapon_equipped_lst=[machinegun2, spitfire1, lazer2, rocketLauncher1]
)

testBT4 = BattleTech(
    tech_type='SHADOW',
    nickname='Scout',
    years_old=11,
    armor_volume=300,
    stamina_capacity=499,
    energy_capacity=90,
    missles_num=5,
    bullets_num=15,
    speed=77,
    armor_slots_num=2,
    weapon_slots_num=3,
    armor_equipped_lst=['', ''],
    weapon_equipped_lst=[machinegun2, lazer3, rocketLauncher3]
)