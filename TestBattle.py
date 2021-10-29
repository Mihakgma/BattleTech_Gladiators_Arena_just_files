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
    """

    # инициализация объекта класса
    def __init__(self,
                 battleTech1,
                 battleTech2,
                 battleTech1Regime='PC',
                 battleTech2Regime='PC'
                 ):
        self.__battleTech1 = battleTech1
        self.__battleTech2 = battleTech2
        self.__battleTech1Regime = battleTech1Regime
        self.__battleTech2Regime = battleTech2Regime

        # вывести на печать информацию по деталям боя
        self.showBTDetails()

    # метод новый раунд
    def startNewRound(self):
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
        # на сколько пунктов снижается урон для 1-ого BattleTech-a
        battleTech1DamageReduction = 0
        # на сколько пунктов снижается урон для 2-ого BattleTech-a
        battleTech2DamageReduction = 0

        # тип урона, который наносит БТ
        damageTypeBT1 = battleTech1Attack[0]
        damageTypeBT2 = battleTech2Attack[0]

        battleTech1Nick = battleTech1.get_nickname()
        battleTech2Nick = battleTech2.get_nickname()

        if battleTech1Defence[0]:
            # Пришло True
            BT1DefenceType = battleTech1Defence[1]
            if BT1DefenceType == 'move' and damageTypeBT2 == 'explosive':
                speedBT1 = battleTech1.get_speed()
                print(f'{battleTech1Nick} пытается уколниться от ракетного залпа на скорости {speedBT1}')
                battleTech1DamageReduction = speedBT1 * 0.35


        if battleTech2Defence[0]:
            # Пришло True
            BT2DefenceType = battleTech2Defence[1]
            if BT2DefenceType == 'move' and damageTypeBT1 == 'explosive':
                speedBT2 = battleTech2.get_speed()
                print(f'{battleTech2Nick} пытается уколниться от ракетного залпа на скорости {speedBT2}')
                battleTech2DamageReduction = speedBT2 * 0.35

        ###

        # обмен уроном в броню
        # thermal damage проходит сквозь физическую броню

        if damageTypeBT1 == 'thermal':
            battleTech2.getStaminaDamage(battleTech1Attack[1] - battleTech2DamageReduction)
        else:
            battleTech2.getArmorDamage(battleTech1Attack[1] - battleTech2DamageReduction)

        if damageTypeBT2 == 'thermal':
            battleTech1.getStaminaDamage(battleTech2Attack[1] - battleTech1DamageReduction)
        else:
            battleTech1.getArmorDamage(battleTech2Attack[1] - battleTech1DamageReduction)

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

    # получить атрибуты
    def get_battleTech1(self):
        return self.__battleTech1

    def get_battleTech2(self):
        return self.__battleTech2

    def get_battleTech1Regime(self):
        return self.__battleTech1Regime

    def get_battleTech2Regime(self):
        return self.__battleTech2Regime
