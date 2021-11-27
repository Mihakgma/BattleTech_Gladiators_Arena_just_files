# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from testBTExamples import *
from TestBattle import Battle1vs1
from time import sleep

def testBattle1(testBTfirst, testBTsecond):
    battleTest1 = Battle1vs1(testBTfirst, testBTsecond)


    roundNum = 0
    while battleTest1.startNewRound:
        #print('###')
        #print()
        roundNum += 1
        #sleep(0.09) # задержка между раундами (опционально)
        #print(f'ROUND {roundNum}')
        #print('###')
        #print()

    # after battle
    BT1ArmorAfter = testBTfirst.get_armor_volume()
    BT2ArmorAfter = testBTsecond.get_armor_volume()
    BT1StaminaAfter = testBTfirst.get_stamina_capacity()
    BT2StaminaAfter = testBTsecond.get_stamina_capacity()

    battleWonBT = 0
    if BT1StaminaAfter == BT2StaminaAfter == 0:
        pass
    elif BT1StaminaAfter > 0 and BT2StaminaAfter == 0:
        battleWonBT = 1
    elif BT2StaminaAfter > 0 and BT1StaminaAfter == 0:
        battleWonBT = 2

    battleResultsLst = [
        battleTest1.get_currentRoundNumber(),
        BT1ArmorAfter,
        BT2ArmorAfter,
        BT1StaminaAfter,
        BT2StaminaAfter,
        battleWonBT
    ]

    #battleResultsTpl = tuple(battleResultsLst)

    return battleResultsLst

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Запускаем тестовый бой!')
    testBattle1(testBT1, testBT5)
    input('Для выхода нажмите клавишу Enter ;-)')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
