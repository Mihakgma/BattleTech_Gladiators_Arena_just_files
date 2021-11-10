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
                 weapon_equipped_lst,
                 inactiveRounds=0,
                 isVisibleNow=1,
                 superabilityToUseNum=1,
                 slowRegenStatus=0,
                 slowRegenToUseNum=1,
                 endedCurrentRound=0
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

           Has a 'GENOCIDE' UNIQUE ability - needs ... energy and ... missiles:

           (mass missles single discharge with a huge explosive damage
           enemy which underwent this ability slows down by 59% during 3 next rounds.
           while this regenerates 35% of armor lost during current battle
           and 75% probability to fix 1 item of weapon and 1 item of armor slot)


        2) SHADOW - weak explosive weaponry (missiles) and metal armour compensates with a huge
           amount of energy capacity as well as fast blasters and precise lazers. Very fast.
           Has a fast machineguns with high percent (25%) of critical strike hits upon an armor.
           Lazer and blaster attacks gives 5.5% probability to destroy (deactivate) any kind of enemy
           slot item (armor or weapon) despite of enemy using or not energy shield!
           Slow regeneration of energy is available during whole the battle
           (need to waste a round to turn it on (only once per battle) -
           insusceptibility to any kind of enemy attack during this round).

           Has a 'HYPERJUMP' UNIQUE ability - needs ... energy & ... stamina:

           (a couple of rounds enemy cant hit him with any kind of weapon.
           while SHADOW can use any kind of ordinar weapon - lasers, blasters, machinegun etc...
           during this regenerates 50% of the original - starting energy capacity
           regenerates 70% of lost stamina capacity
           on a last round of it - hits enemy with a shock -
           70% probability of enemy move skipping during 3 next rounds
           and 75% probability to fix 1 item of weapon and 1 item of armor slot of SHADOW)


        3) INFERNO - medium missiles force, weak lazers but has machinegun with medium damage.
           Can use a spitfire which ignores metal armor (but quickly destroy it ?) and penetrates
           on 45% through any kind of energy shield.
           Fire attacks gives 3.5% probability to destroy any kind of enemy
           slot item (armor or weapon) despite of enemy using or not energy shield!
           Slow regeneration of stamina is available during whole the battle
           (need to waste a round to turn it on (only once per battle) -
           insusceptibility to any kind of enemy attack during this round).
           Slow regeneration of energy is available during whole the battle
           (need to waste a round to turn it on (only once per battle) -
           insusceptibility to any kind of enemy attack during this round).

           Has a 'HELL' UNIQUE ability - needs ... energy & ... bullets:
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
        4) MANTIS - medium BattleTech. Uses lazers and rocket launchers.
           Has a 'FREEZE' UNIQUE ability - needs 55 energy:
           ()

        5) WASP - light BattleTech. Very fast, with medium amount of machinegun
           and lazer ammo (energy). Machinegun with prob 7.9% deactivates enemy slow regeneration.
           Lazer and blaster attacks gives 3.5% probability to deactivate one weapon item
           (the one with the most damage points)!
           Slow regeneration of energy is available during whole the battle
           (need to waste a round to turn it on (only once per battle) -
           insusceptibility to any kind of enemy attack during this round).

           Has a 'POISONOUS STING' UNIQUE ability - needs 39 energy & 33 bullets:
           (
           add poison to machinegun bullets for the rest of the battle.
           poison makes additional damage (27% of the basic bullets damage)
           which ignores armor, phisical or even energy shields
           )


           ...
           Length of armor and weapon lists cant be more than
           armor_slots_num and weapon_slots_num accordingly.
           If Len of one of the lists is bigger of the slots number or < 1 so the warning message
           pops before the initialization of the current class object.
           And the initialization process cant be performed!

        """
        stamina_capacity = round(stamina_capacity, 2)
        energy_capacity = round(energy_capacity, 2)

        self.__tech_type = tech_type
        self.__nickname = nickname
        self.__years_old = years_old
        self.__armor_volume = armor_volume
        self.__stamina_capacity = stamina_capacity
        self.__energy_capacity = energy_capacity
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

        # save baseline attribute levels
        self.__baseline_armor_volume = armor_volume
        self.__baseline_stamina_capacity = stamina_capacity
        self.__baseline_energy_capacity = energy_capacity
        self.__baseline_missiles_num = missles_num
        self.__baseline_bullets_num = bullets_num
        self.__baseline_speed = speed

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

    def set_inactiveRounds(self, inactiveRounds):
        self.__inactiveRounds = inactiveRounds

    def set_isVisibleNow(self, isVisibleNow):
        self.__isVisibleNow = isVisibleNow

    def set_superabilityToUseNum(self, superabilityToUseNum):
        self.__superabilityToUseNum = superabilityToUseNum

    def set_slowRegenStatus(self, slowRegenStatus):
        self.__slowRegenStatus = slowRegenStatus

    def set_slowRegenToUseNum(self, slowRegenToUseNum):
        self.__slowRegenToUseNum = slowRegenToUseNum

    def set_endedCurrentRound(self, endedCurrentRound):
        self.__endedCurrentRound = endedCurrentRound


    def refreshStats(
            self,
            armor_volume,
            stamina_capacity,
            energy_capacity,
            missles_num,
            bullets_num,
            speed,
            inactiveRounds=0,
            isVisibleNow=1,
            superabilityToUseNum=1,
            slowRegenStatus=0,
            slowRegenToUseNum=1,
            endedCurrentRound=0
                     ):
        self.__armor_volume = armor_volume
        self.__stamina_capacity = stamina_capacity
        self.__energy_capacity = energy_capacity
        self.__missles_num = missles_num
        self.__bullets_num = bullets_num
        self.__speed = speed
        self.__inactiveRounds = inactiveRounds
        self.__isVisibleNow = isVisibleNow
        self.__superabilityToUseNum = superabilityToUseNum
        self.__slowRegenStatus = slowRegenStatus
        self.__slowRegenToUseNum = slowRegenToUseNum
        self.__endedCurrentRound = endedCurrentRound


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

    def get_inactiveRounds(self):
        return self.__inactiveRounds

    def get_isVisibleNow(self):
        return self.__isVisibleNow

    def get_superabilityToUseNum(self):
        return self.__superabilityToUseNum

    def get_slowRegenStatus(self):
        return self.__slowRegenStatus

    def get_slowRegenToUseNum(self):
        return self.__slowRegenToUseNum

    def get_endedCurrentRound(self):
        return self.__endedCurrentRound

    # get baseline attribute levels
    def get_baseline_armor_volume(self):
        return self.__baseline_armor_volume

    def get_baseline_stamina_capacity(self):
        return self.__baseline_stamina_capacity

    def get_baseline_energy_capacity(self):
        return self.__baseline_energy_capacity

    def get_baseline_missiles_num(self):
        return self.__baseline_missiles_num

    def get_baseline_bullets_num(self):
        return self.__baseline_bullets_num

    def get_baseline_speed(self):
        return self.__baseline_speed


    # print all atributes by doing 1 method
    def showAllAttrValues(self):
        """
        show eg print values
        of all attributes of the current
        BattleTech one
        """
        noYesLst = ['Нет', 'Да']
        offOnLst = ['Выкл', 'Вкл']

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
        print(f'BattleTech пропускает ход следующие {self.get_inactiveRounds()} раундов!')
        print(f'Виден противником: {noYesLst[self.get_isVisibleNow()]}')
        print(f'Может использовать уникальную способность {self.get_superabilityToUseNum()} раз')
        print(f'Режим медленной регенерации: {offOnLst[self.get_slowRegenStatus()]}')
        print(f'Может активировать режим медленной регенерации: {self.get_slowRegenToUseNum()} раз')
        print(f'Закончил текущий раунд: {noYesLst[self.get_endedCurrentRound()]}')


    # БОЕВКА
    # МЕТОДЫ ЗАЩИТЫ
    def move(self):
        """
        Передвигает робота (уклонение)
        эффективно от ракетного залпа и атаки огнеметом,
        т.к. это медленные типы оружия
        """
        passRounds = self.get_inactiveRounds()
        currentSpeed = self.get_speed()
        currentNickname = self.get_nickname()
        endedCurrentRound = self.get_endedCurrentRound()

        if passRounds > 0: # пропуск раунда
            print(f'{currentNickname} не может стронуться с места!')
            print('Reason: pass round!')
            self.__inactiveRounds -= 1
            return False, 'move'
        elif endedCurrentRound == 1: # уже закончил раунд!
            print(f'{currentNickname} не может стронуться с места!')
            print('Reason: already ended this round!')
            return False, 'move'
        elif currentSpeed > 0:
            #print(f'{currentNickname} применяет уклонение на скорости {currentSpeed}')
            return True, 'move'
        else:
            print(f'{currentNickname} не может стронуться с места!')
            print('Reason: Not enough speed!')
            return False, 'move'

    def becomeInvulnerable(self):
        return True, 'invulnerable'


    def activateEnergyShield(self):
        """
        Активизирует энергетический щит.
        Эффективен против лазеров (?) и Огнеметов.
        может быть применен только если у BattleTech-а осталась энергия
        """
        passRounds = self.get_inactiveRounds()
        endedCurrentRound = self.get_endedCurrentRound()

        if passRounds > 0: # пропуск раунда
            print(f'{self.get_nickname()} не может активировать энергетический щит!')
            print('Reason: pass round!')
            self.__inactiveRounds -= 1
            return False, 'energy shield'
        elif endedCurrentRound == 1: # уже закончил раунд!
            print(f'{self.get_nickname()} не может активировать энергетический щит!')
            print('Reason: already ended this round!')
            return False, 'energy shield'
        elif self.get_energy_capacity() > 0:
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
        passRounds = self.get_inactiveRounds()
        endedCurrentRound = self.get_endedCurrentRound()

        if passRounds > 0: # пропуск раунда
            print(f'{self.get_nickname()} не может активировать физический щит!')
            print('Reason: pass round!')
            self.__inactiveRounds -= 1
            return False, 'phisical shield'
        elif endedCurrentRound == 1: # уже закончил раунд!
            print(f'{self.get_nickname()} не может активировать физический щит!')
            print('Reason: already ended this round!')
            return False, 'phisical shield'
        elif self.get_armor_volume() > 0:
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

        passRounds = self.get_inactiveRounds()
        endedCurrentRound = self.get_endedCurrentRound()
        currentNickname = self.get_nickname()

        if passRounds > 0:  # пропуск раунда
            print(f'{currentNickname} не может использовать оружие!')
            print('Reason: pass round!')
            self.__inactiveRounds -= 1
            return '', 0
        elif endedCurrentRound == 1: # уже закончил раунд!
            print(f'{currentNickname} не может использовать оружие!')
            print('Reason: already ended this round!')
            return '', 0

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
            elif chosen_weapon.get_activeStatus() == 0:
                print(f'{currNickname} пытается использовать {currWeapon}!')
                print('Орудие выведено из строя!')
                return False
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
        print(f'Weapon fail probs border: {currWeaponFailProbability} '
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

    def superAbilityOtherRequirementsAccepted(self):
        """
        """
        pass


    # Unique abilities methods
    def activateUniqueAbility(self):
                              #superabilityotherRequirementsAccepted: bool=False):
        superAbilityOtherRequirementsAccepted = self.superAbilityOtherRequirementsAccepted()
        passRounds = self.get_inactiveRounds()
        superabilityToUseNum = self.get_superabilityToUseNum()
        nickName = self.get_nickname()
        endedCurrentRound = self.get_endedCurrentRound()

        if passRounds > 0:  # пропуск раунда
            print(f'{nickName} не может использовать уникальную способность!')
            print('Reason: pass round!')
            self.__inactiveRounds -= 1
            return False
        elif endedCurrentRound == 1:  # уже закончил раунд!
            print(f'{nickName} не может использовать уникальную способность!')
            print('Reason: already ended this round!')
            return False
        elif superabilityToUseNum < 1:
            print(f'{nickName} не может использовать уникальную способность!')
            print('Reason: already used it!')
            return False
        elif (superabilityToUseNum > 0
              and superAbilityOtherRequirementsAccepted):
            print(f'{nickName} использует уникальную способность!')
            self.__superabilityToUseNum -= 1
            #self.__endedCurrentRound = 1
            return True
        else:
            print(f'{nickName} не может использовать уникальную способность!')
            print('Reason: other requirements didnt accepted!')
            return False

    # activate slow regeneration method
    def activateSlowRegen(self):
        """
        checks if slow regen is possible.
        if it is possible renew some attributes values:
        slowRegenStatus = 1
        slowRegenToUseNum -= 1
        endedCurrentRound = 1
        :return: bool
        """
        passRounds = self.get_inactiveRounds()
        nickName = self.get_nickname()
        slowRegenStatus = self.get_slowRegenStatus()
        slowRegenToUseNum = self.get_slowRegenToUseNum()
        endedCurrentRound = self.get_endedCurrentRound()

        if passRounds > 0:  # пропуск раунда
            print(f'{nickName} не может активировать медленную регенерацию!')
            print('Reason: pass round!')
            self.__inactiveRounds -= 1
            return False
        elif endedCurrentRound == 1:  # уже закончил раунд!
            print(f'{nickName} не может активировать медленную регенерацию!')
            print('Reason: already ended this round!')
            return False
        elif (slowRegenStatus == 0 and
         slowRegenToUseNum > 0 and
         endedCurrentRound == 0):
            print(f'{nickName} активирует медленную регенерацию!')
            self.__slowRegenStatus = 1
            self.__slowRegenToUseNum -= 1
            #self.__endedCurrentRound = 1
            return True

    def slowRegenGetBonus(self):
        """"
        If slow regen is activated (this or one of prev round)
        BT is getting stamina or armor or energy bonuses!

        ATTENTION!
        this bonus cannot be greater then current variable (attribute) baseline value!
        """

        staminaBonus = 3
        armorBonus = 5
        energyBonus = 1
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
