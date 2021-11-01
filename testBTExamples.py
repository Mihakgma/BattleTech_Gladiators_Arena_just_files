from WeaponsExample import *
from Robots import BattleTech

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
    nickname='Sparky',
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

testBT5 = BattleTech(
    tech_type='INFERNO',
    nickname='Leviathan',
    years_old=666,
    armor_volume=666,
    stamina_capacity=666,
    energy_capacity=666,
    missles_num=666,
    bullets_num=666,
    speed=5,
    armor_slots_num=3,
    weapon_slots_num=9,
    armor_equipped_lst=['', '', ''],
    weapon_equipped_lst=[machinegun1, spitfire1, lazer1, rocketLauncher1,
                         machinegun2, lazer2, rocketLauncher3, lazer3, rocketLauncher2]
)