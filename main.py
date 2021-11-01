# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from testBTExamples import *
from TestBattle import Battle1vs1
from time import sleep

def testBattle1():
    battleTest1 = Battle1vs1(testBT1, testBT5)
    roundNum = 0
    while battleTest1.startNewRound():
        print('###')
        print()
        roundNum += 1
        sleep(0.09) # задержка между раундами (опционально)
        print(f'ROUND {roundNum}')
        print('###')
        print()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Запускаем тестовый бой!')
    testBattle1()
    input('Для выхода нажмите клавишу Enter ;-)')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
