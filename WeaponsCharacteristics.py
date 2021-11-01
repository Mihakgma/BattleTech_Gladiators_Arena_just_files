from Weaponry import Weapon

damageTypeLst = [
    'phisical',
    'explosive',
    'thermal',
    'energetic'
]

weaponInfoDict = {

    0:
        [
                'Крупнокалиберный пулемет',
                damageTypeLst[0],
                11,
                100,
                25,
                'Крупнокалиберный пулемет готов обрушить свинцовый шквал на врага!'
        ],
    1:
        [
                'Гаубица',
                damageTypeLst[0],
                33,
                100,
                99,
                'Гаубица - это та же пушка, но побольше размером!'
        ],
    2:
        [
                'Плазменный бластер',
                damageTypeLst[3],
                57,
                100,
                61,
                'С БаттлТехом, вооруженным плазменным бластером шутки плохи...'
        ],
    3:
        [
                'Ракетная установка',
                damageTypeLst[1],
                19,
                100,
                39,
                'Переносная пусковая ракетная установка, установленная на БаттлТех, вполне заслуженно '
                'считается весомым аргументом, как в прямом, так и в переносном смысле.'
        ],
    4:
        [
                'Толстяк',
                damageTypeLst[1],
                111,
                100,
                95,
                'Толстяк - незамысловатое наименование крупнокалиберной ракетной установки.'
                ' Тонкий намек на ТОЛСТЫЕ обстоятельства!'
        ],
    5:
        [
                'Огнемет',
                damageTypeLst[2],
                79,
                100,
                71,
                'Огнемет. Семь бед - один ответ! '
        ],
    6:
        [
                'Станковый пулемет',
                damageTypeLst[0],
                5,
                100,
                11,
                'Обычный станковый пулемет...'
        ],
    7:
        [
                'Промышленная резка',
                damageTypeLst[3],
                89,
                100,
                130,
                'Промышленная резка. Представляет собой усовершенствованную версию лазера, '
                'используемого в тяжелой промышленности.'
        ],
    8:
        [
                'Катюша',
                damageTypeLst[1],
                41,
                100,
                63,
                'Что может быть лучше старой боевой "подруги"?'
                'Катюша не даст заскучать ни своему хозяину, ни тем более, его противнику!'
        ],
    9:
        [
                'Контрактный бластер',
                damageTypeLst[3],
                19,
                100,
                149,
                'Востановленный и отрегулированный. Можно сказать, восставший из пепла '
                'контрактный бластер является одним из самых ходовых '
                '(что вполне заслуженно) современных видов вооружения.'
        ]
}


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    def farewell():
        print('ВСЕГО ХОРОШЕГО!')
        input('Для выхода нажмите клавишу Enter ;-)')

    print('В данном скрипте хранится инфа по оружию, ')
    print('упорядоченная в виде словаря!')
    print('ключ - порядковый номер, а значения зашифрованы в виде списка')
    print('содержимое списка: наименование, вид урона, возраст (лет), прочность, урон (пунктов)')

    print(f'Количество орудий в арсенале на данный момент: {len(weaponInfoDict)} ед.')

    printDictContains = input('Вывести на печать все содержимое оружейного арсенала (y/n)? ')
    printDictContains = printDictContains.strip().lower()
    if ('н' in printDictContains or
        'n' in printDictContains):
        pass

    else:
        for weaponKey in weaponInfoDict:
            currWeapInfoLst = weaponInfoDict[weaponKey]
            currWeaponObj = Weapon(
                damage_type=currWeapInfoLst[1],
                name=currWeapInfoLst[0],
                years_old=currWeapInfoLst[2],
                endurance_volume=currWeapInfoLst[3],
                damage_points=currWeapInfoLst[4]
            )
            currWeaponObj.getAllAttributes()
            print(f'Дополнительная информация: \n{currWeapInfoLst[5]}\n')

    farewell()