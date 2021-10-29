# тестовый запуск класса
from Robots import *
from Weaponry import *

def CreateTestBT():
    # Локальные переменные
    tech_type = ""
    tech_type_lst = [
        'GLADIATOR',
        'SHADOW',
        'INFERNO'
    ]
    nickname = ""
    years_old = 0
    armor_volume = 0
    stamina_capacity = 0
    energy_capacity = 0
    missles_num = 0
    bullets_num = 0
    speed = 0
    armor_slots_num = 0
    weapon_slots_num = 0
    armor_equipped_lst = []
    weapon_equipped_lst = []

    # Получить данные о BattleTech.

    print()

    counter = 0
    for battleTechType in tech_type_lst:
        counter += 1
        print(f'{counter} - {battleTechType}')

    while True:
        try:
            tech_type_index = int(input('Выберите один из вышеказанных видов BattleTech (введите цифру): ')) - 1
            tech_type = tech_type_lst[tech_type_index]
            break
        except:
            print('Что-то пошло не так... Попробуйте повторить выбор Вашего BattleTech')

    print(f'Вы выбрали {tech_type}!')
    print()

    nickname = input('Введите ник BattleTech: ')

    years_old = int(input('Возраст BattleTech (лет): '))

    armor_volume = int(input('Объем брони BattleTech (пунктов): '))
    stamina_capacity = int(input('Стамина BattleTech (пунктов): '))
    energy_capacity = int(input('Энергия BattleTech (пунктов): '))
    missles_num = int(input('Боезапас ракет BattleTech (штук): '))
    bullets_num = int(input('Боезапас патронов BattleTech (штук): '))
    speed = stamina_capacity = int(input('Скорость BattleTech (км/ч): '))
    armor_slots_num = int(input('Слотов брони BattleTech (штук): '))
    weapon_slots_num = int(input('Слотов оружия BattleTech (штук): '))
    print()

    weapon_lst = [
        machinegun1,
        machinegun2,
        rocketLauncher1,
        rocketLauncher2,
        lazer1,
        lazer2,
        cannon1,
        spitfire1
    ]

    # пока что класс брони, которую экипируют на BattleTech-и не был создан,
    # экипируем его вымышленной броней, которая представляет собой простую строку
    for armor_unit_index in range(armor_slots_num):
        armor_equipped_lst.append(input('Название единицы брони: '))
    print()
    for weapon_unit_index in range(weapon_slots_num):
        counter = 0
        #print([str(counter += 1) + weapon.get_name() for weapon in weapon_lst])
        for weapon in weapon_lst:
            counter += 1
            print(str(counter), weapon.get_name())
        weapon_equipped_lst.append(weapon_lst[int(input('Порядковый номер единицы оружия: ')) - 1])

    print()
    print()
    print()

    # Создать экземпляр класса BattleTech.
    myTestBattleTech = BattleTech(
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
    )

    # Показать все введенные данные.
    print('Параметры тестового BattleTech: ')
    myTestBattleTech.showAllAttrValues()

    return myTestBattleTech

if __name__ == '__main__':
    # Вызвать тестовую функцию.
    CreateTestBT()
    input('Для выхода нажмите клавишу Enter ;-)')