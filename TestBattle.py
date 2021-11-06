from random import randint as random_randint

class Battle1vs1():
    """
    methods:
    1) startNewRound()
    2) endBattle()
    3) simpleAI()
    4) manualPiloting()
    5) showBTDetails() - before battle.
    6) applyRoundActions() - apply chosen actions by both BattleTechs.

    attributes:
    1) BT1, BT2 - objects;
    2) BT1-, BT2 - regimes (PC, manual);
    3) number of current round (currentRoundNumber - positive integer)
    """

    # инициализация объекта класса
    def __init__(self,
                 battleTech1,
                 battleTech2,
                 battleTech1Regime='PC',
                 battleTech2Regime='PC',
                 currentRoundNumber:int=0):
        self.__battleTech1 = battleTech1
        self.__battleTech2 = battleTech2
        self.__battleTech1Regime = battleTech1Regime
        self.__battleTech2Regime = battleTech2Regime
        self.__currentRoundNumber = currentRoundNumber

        # вывести на печать информацию по деталям боя
        self.showBTDetails()

    # метод новый раунд
    def startNewRound(self):

        # automatically increment number of current round attribute
        self.__currentRoundNumber += 1

        battleTech1Regime = self.get_battleTech1Regime()
        battleTech2Regime = self.get_battleTech2Regime()
        battleTech1 = self.get_battleTech1()
        battleTech2 = self.get_battleTech2()

        if battleTech1Regime == 'PC':
            battleTech1AttackDefend = self.simpleAI(battleTech1)
            battleTech1Attack = battleTech1AttackDefend[0]
            battleTech1Defence = battleTech1AttackDefend[1]

        elif battleTech1Regime == 'manual':
            self.manualPiloting(battleTech1)

        if battleTech2Regime == 'PC':
            battleTech2AttackDefend = self.simpleAI(battleTech2)
            battleTech2Attack = battleTech2AttackDefend[0]
            battleTech2Defence = battleTech2AttackDefend[1]

        elif battleTech2Regime == 'manual':
            self.manualPiloting(battleTech2)

        # здесь будет код для типа уклонения у каждого БТ!
        ###
        # прописать метод возвращающий battleTechDamageReduction для обоих BT!
        # get_battleTechDamageReduction()
        # на сколько пунктов снижается урон для 1-ого BattleTech-a
        battleTech1DamageReduction = 0
        # на сколько пунктов снижается урон для 2-ого BattleTech-a
        battleTech2DamageReduction = 0

        # тип урона, который наносит БТ
        damageTypeBT1 = battleTech1Attack[0]
        damageTypeBT2 = battleTech2Attack[0]

        battleTech1Nick = battleTech1.get_nickname()
        battleTech2Nick = battleTech2.get_nickname()

        def printDefenceType(
                BTNickname,
                BTDefenceType
        ):
            print(f'{BTNickname} выбрал защиту с помощью {BTDefenceType}!')

        if battleTech1Defence[0]:
            # Пришло True из метода защиты класса BT
            # Вызов метода расчета объема снижения урона
            BT1DefenceType = battleTech1Defence[1]
            printDefenceType(battleTech1Nick, BT1DefenceType)
            battleTech1DamageReduction=self.get_battleTechDamageReduction(
                BTdefender=battleTech1,
                BTdefenderDefenceType=BT1DefenceType,
                BTattackerDamageType=damageTypeBT2,
                BTdefenderNickname=battleTech1Nick,
                BTattackerNickname=battleTech2Nick,
                damagePointsGot=battleTech2Attack[1]
            )


        if battleTech2Defence[0]:
            # Пришло True
            BT2DefenceType = battleTech2Defence[1]
            printDefenceType(battleTech2Nick, BT2DefenceType)
            battleTech2DamageReduction = self.get_battleTechDamageReduction(
                BTdefender=battleTech2,
                BTdefenderDefenceType=BT2DefenceType,
                BTattackerDamageType=damageTypeBT1,
                BTdefenderNickname=battleTech2Nick,
                BTattackerNickname=battleTech1Nick,
                damagePointsGot=battleTech1Attack[1]
            )

        ###

        # обмен уроном в броню
        # thermal damage проходит сквозь физическую броню
        battleTech2DamageGot = round(battleTech1Attack[1] - battleTech2DamageReduction, 2)
        battleTech1DamageGot = round(battleTech2Attack[1] - battleTech1DamageReduction, 2)

        if damageTypeBT1 == 'thermal':
            battleTech2.getStaminaDamage(battleTech2DamageGot)
        else:
            battleTech2.getArmorDamage(battleTech2DamageGot)

        if damageTypeBT2 == 'thermal':
            battleTech1.getStaminaDamage(battleTech1DamageGot)
        else:
            battleTech1.getArmorDamage(battleTech1DamageGot)

        # проверяем стамину роботов и определяем окончен бой или нет?
        battleTech1Stamina = battleTech1.get_stamina_capacity()
        battleTech2Stamina = battleTech2.get_stamina_capacity()
        if battleTech1Stamina < 1 or battleTech2Stamina < 1:

            battleTech1Info = battleTech1.showAllAttrValues()
            battleTech2Info = battleTech2.showAllAttrValues()
            # 1-ый вариант - 1-ый и 2-ой БатлТех-и вышли из строя ОДНОВРЕМЕННО!
            if battleTech1Stamina < 1 and battleTech2Stamina < 1:
                print(f'Бой между {battleTech1Nick} и {battleTech2Nick} окончен - НИЧЬЯ (оба вышли из строя)!')
                print(battleTech1Info)
                print(battleTech2Info)
            # 2-ой вариант - 1-ый БатлТех вышел из строя!
            elif battleTech1Stamina < 1:
                print(f'Бой окончен победой {battleTech2Nick} !')
            # 3-ий вариант - 2-ой БатлТех вышел из строя!
            elif battleTech1Stamina < 1:
                print(f'Бой окончен победой {battleTech1Nick} !')

            return False
        else:
            return True

    def get_battleTechDamageReduction(
            self,
            BTdefender: object,
            #BTattacker: object,
            BTdefenderDefenceType: str,
            BTattackerDamageType: str,
            BTdefenderNickname: str,
            BTattackerNickname: str,
            damagePointsGot: int
    ):
        """"
        BTdefender - BT that gets damage (damage receipient)
        BTattacker - BT that make damage (damage donor)

        This method gets as input:
        1) BTdefender's type of defence
        2) BTattacker's type of damage
        3) BTdefender's nickname
        4) BTattacker's nickname

        This method produce an output:
        BTdefenderDamageReduction - int (in range 0:999)

        var BTdefenderDamageReduction cannot be a negative int (less than 0) - ???

        1) dodgeCoeff - constant var coeff of reduction of damage in a case of:
        BTattacker's type of damage is 'explosive'
        & (logical expression)
        BTdefender's type of defence is 'move'

        etc on the same template the other defence-damage pairs!

        2) energyShieldEnergeticDamageResistCoeff
        3) energyShieldThermalResistCoeff
        4) physicalResistCoeff


        """
        dodgeCoeff = 0.45
        energyShieldEnergeticDamageResistCoeff = 0.83
        energyShieldThermalResistCoeff = 0.55
        physicalResistCoeff = 0.69

        BTdefenderDamageReduction = 0

        if BTdefenderDefenceType == 'move' and BTattackerDamageType == 'explosive':
            # need get defender's speed
            speedBTdefender = BTdefender.get_speed()
            print(f'{BTdefenderNickname} пытается уколниться от '
                  f'ракетного залпа {BTattackerNickname} на скорости {speedBTdefender} км/ч')
            BTdefenderDamageReduction = speedBTdefender * dodgeCoeff

        elif BTdefenderDefenceType == 'move' and BTattackerDamageType == 'thermal':
            # need get defender's speed
            speedBTdefender = BTdefender.get_speed()
            print(f'{BTdefenderNickname} пытается уколниться от '
                  f'атаки огнеметом {BTattackerNickname} на скорости {speedBTdefender} км/ч')
            BTdefenderDamageReduction = speedBTdefender * dodgeCoeff

        elif BTdefenderDefenceType == 'energy shield' and BTattackerDamageType == 'energetic':
            # successful defence!
            BTdefenderDamageReduction = damagePointsGot * energyShieldEnergeticDamageResistCoeff
            print(f'{BTdefenderNickname} успешно активировал энергетический щит '
                  f'против <{BTattackerDamageType}> атаки {BTattackerNickname},'
                  f' снизив урон на {BTdefenderDamageReduction} пунктов!')

        elif BTdefenderDefenceType == 'energy shield' and BTattackerDamageType == 'thermal':
            # successful defence!
            BTdefenderDamageReduction = damagePointsGot * energyShieldThermalResistCoeff
            print(f'{BTdefenderNickname} успешно активировал энергетический щит '
                  f'против <{BTattackerDamageType}> атаки {BTattackerNickname}, '
                  f' снизив урон на {BTdefenderDamageReduction} пунктов!')


        elif BTdefenderDefenceType == 'phisical shield' and BTattackerDamageType == 'phisical':
            # successful defence!
            BTdefenderDamageReduction = damagePointsGot * physicalResistCoeff
            print(f'{BTdefenderNickname} успешно активировал физический щит '
                  f'против <{BTattackerDamageType}> атаки {BTattackerNickname}, '
                  f' снизив урон на {BTdefenderDamageReduction} пунктов!')

        else:
            print(f'{BTdefenderNickname} не удалось выбрать эффективную защиту '
                  f'против атаки {BTattackerNickname} :-(')



        return BTdefenderDamageReduction



    def showBTDetails(self):
        battleTech1 = self.get_battleTech1()
        battleTech2 = self.get_battleTech2()
        print(f'БОЙ {battleTech1.get_nickname()} против {battleTech2.get_nickname()} !')
        # вывести инфу по тому, кто управляет каждым Роботом!
        print()
        print(f'Режим управления {battleTech1.get_nickname()}: {self.get_battleTech1Regime()}')
        print(f'Режим управления {battleTech2.get_nickname()}: {self.get_battleTech2Regime()}')
        print()
        print()

    def simpleAI(self, currentBattleTech: object):
        # print(f'{currentBattleTech.get_nickname()} управляет ИИ')
        # реализация урона случайным орудием
        weaponList = currentBattleTech.get_weapon_equipped_lst()
        randomWeaponLstIndex = random_randint(0, len(weaponList) - 1)
        damageChosen = currentBattleTech.use_weapon_by_lst_index(randomWeaponLstIndex)

        # лист возможных вариантов защиты
        #defenceList =
        randomDefenseLstIndex: int = random_randint(0, 2)
        defenceChosen = [
            currentBattleTech.move(),
            currentBattleTech.activateEnergyShield(),
            currentBattleTech.activatePhisicalShield()
        ][randomDefenseLstIndex]
        return [damageChosen, defenceChosen]

    def manualPiloting(self, currentBattleTech):
        # print(f'{currentBattleTech.get_nickname()} управляет пользователь')
        pass

    # задать атрибуты
    def set_battleTech1(self, battleTech1):
        self.__battleTech1 = battleTech1

    def set_battleTech2(self, battleTech2):
        self.__battleTech2 = battleTech2

    def set_battleTech1Regime(self, battleTech1Regime):
        self.__battleTech1Regime = battleTech1Regime

    def set_battleTech2Regime(self, battleTech2Regime):
        self.__battleTech2Regime = battleTech2Regime

    def set_currentRoundNumber(self, currentRoundNumber):
        self.__currentRoundNumber = currentRoundNumber

    # получить атрибуты
    def get_battleTech1(self):
        return self.__battleTech1

    def get_battleTech2(self):
        return self.__battleTech2

    def get_battleTech1Regime(self):
        return self.__battleTech1Regime

    def get_battleTech2Regime(self):
        return self.__battleTech2Regime

    def get_currentRoundNumber(self):
        return self.__currentRoundNumber
