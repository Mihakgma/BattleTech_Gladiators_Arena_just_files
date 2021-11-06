from testBTExamples import *
from itertools import combinations
from main import testBattle1
#from TestBattle import Battle1vs1
import pandas as pd

BTdictToDuel = {
    testBT1: [testBT1.get_nickname()],
    testBT2: [testBT2.get_nickname()],
    testBT3: [testBT3.get_nickname()],
    testBT4: [testBT4.get_nickname()],
    testBT5: [testBT5.get_nickname()]
}

def allBTduelsXtimes(
        BTdict,
        battleIterationsPerBTPair: int=100
):
    """"
    returns df with battle results
    """
    BTuniqueSet = set()

    for elemObj in BTdictToDuel:
        BTuniqueSet.add(elemObj)

    #print(BTuniqueSet)

    BTobjPairly = []
    for pair in combinations(BTuniqueSet, r=2):
        #print(pair)
        BTobjPairly.append(pair)

    #print(BTobjPairly)

    dfResults = pd.DataFrame({
        'BT1nick': [],
        'BT2nick': [],
        'BT1Type': [],
        'BT2Type': [],
        'BT1ArmorBefore': [],
        'BT2ArmorBefore': [],
        'BT1StaminaBefore': [],
        'BT2StaminaBefore': [],
        'Total num of Rounds': [],
        'BT1ArmorAfter': [],
        'BT2ArmorAfter': [],
        'BT1StaminaAfter': [],
        'BT2StaminaAfter': [],
        'battleWonBT': []
    })

    counterBattleNum = 0
    for BTobjPair in BTobjPairly:
        BTnumOne = BTobjPair[0]
        BTnumTwo = BTobjPair[1]

        BT1nick = BTnumOne.get_nickname()
        BT2nick = BTnumTwo.get_nickname()
        BT1Type = BTnumOne.get_tech_type()
        BT2Type = BTnumTwo.get_tech_type()
        BT1ArmorBefore = BTnumOne.get_armor_volume()
        BT2ArmorBefore = BTnumTwo.get_armor_volume()
        BT1StaminaBefore = BTnumOne.get_stamina_capacity()
        BT2StaminaBefore = BTnumTwo.get_stamina_capacity()
        BT1EnergyBefore = BTnumOne.get_energy_capacity()
        BT2EnergyBefore = BTnumTwo.get_energy_capacity()
        BT1MisslesBefore = BTnumOne.get_missles_num()
        BT2MisslesBefore = BTnumTwo.get_missles_num()
        BT1BulletsBefore = BTnumOne.get_bullets_num()
        BT2BulletsBefore = BTnumTwo.get_bullets_num()
        BT1SpeedBefore = BTnumOne.get_speed()
        BT2SpeedBefore = BTnumTwo.get_speed()

        battletLst = [
            BT1nick,
            BT2nick,
            BT1Type,
            BT2Type,
            BT1ArmorBefore,
            BT2ArmorBefore,
            BT1StaminaBefore,
            BT2StaminaBefore
        ]

        for battlePerPairNum in range(battleIterationsPerBTPair):
            counterBattleNum += 1
            currBattleResultsLst = testBattle1(testBTfirst=BTnumOne, testBTsecond=BTnumTwo)
            BTnumOne.refreshStats(
                armor_volume=BT1ArmorBefore,
                stamina_capacity=BT1StaminaBefore,
                energy_capacity=BT1EnergyBefore,
                missles_num=BT1MisslesBefore,
                bullets_num=BT1BulletsBefore,
                speed=BT1SpeedBefore
            )
            BTnumTwo.refreshStats(
                armor_volume=BT2ArmorBefore,
                stamina_capacity=BT2StaminaBefore,
                energy_capacity=BT2EnergyBefore,
                missles_num=BT2MisslesBefore,
                bullets_num=BT2BulletsBefore,
                speed=BT2SpeedBefore
            )
            # формируем новую строку ДФ, состоящий из некоторых характеристик
            # БатлТехов перед и после дуэли!
            dfResults.loc[counterBattleNum] = battletLst + currBattleResultsLst

    return dfResults

if __name__ == '__main__':
    print('Запускаем тестовые бои с заданным количеством итераций!'
          'результат боев записывается в Excel-файл с заданным названием в рабочей директории')
    BattleNum = int(input('Введите количество итераций для боя по каждой паре BattleTech-ов: '))
    df = allBTduelsXtimes(BTdict=BTdictToDuel, battleIterationsPerBTPair=BattleNum)
    df.to_excel(f'{BattleNum}_BattlesResults.xlsx', index=True)
