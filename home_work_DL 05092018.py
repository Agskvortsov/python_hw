# Task 1
# У вас есть вложенный список чисел. НАпишите функцию генератор который вернет все элементы коллекции по очереди.

import collections

items = [1, 2, [3, 4, [5, 6], 7], 8]

def flatten(l):
    for el in l:
        if isinstance(el, collections.Iterable):
            for sub in flatten(el):
                yield sub
        else:
            yield el

for elem in flatten(items):
    print(elem)



gen = flatten(items)
next(gen)
next(gen)
print(next(gen))
print(next(gen))
next(gen)
print(next(gen))
next(gen)





# # Task 4
# Игра морской бой. Ваша задача:
#
# Вам нужно сгенерировать поле заданого размера вида где 0 это свободные ячейки. Например поле с размером 5:
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
#
# Рандомно разместить корабли (однопалубные ). Когда вы размещаете корабль на ваше поле, 0 меняется на 1. У вас должна
#  быть возможность задавать количество кораблей которые необходимо разместить, но не более чем n-1 от всех ячеек вашего
#  поля. После этого предложите ввести пользователю номер строки и номер столбца для выстрела. Если он попал,
# проинформируйте его об этом и замените 1 на 0.
#
# Продолжайте игру до тех пор пока не будут уничтожены все корабли или сделайте ограничение на количество выстрелов.
import copy

def start_game():
    global desk_size
    desk_size = int(input('Подалуйста введите размер игрового поля(цифра от 2 до 10)'))
    qtty_of_warships = int(input('Пожалуйста введите количество кораблей '
                                 'на поле(цифра от 1 до {})'.format(desk_size**2-1)))
    if qtty_of_warships > desk_size**2 - 1:
        qtty_of_warships = desk_size**2 - 1
    game_desk_dict, fields_list = create_game_desk(desk_size)
    # Под конец решил распечатать в конце игры начальное состояние доски(start_game_desk_dict), но столкнулся с
    # проблемой. Не могу сделать отдельную копию словаря. Три способа перепробовал,а он все равно друг на game_desk_dict
    #  ссылаются. Может какие-то настройки интепритатора...
    start_game_desk_dict = {**game_desk_dict}
    fill_up_game_desk_by_warships(game_desk_dict, qtty_of_warships, fields_list)
    shoot_results_dict = create_game_desk(desk_size)[0]
    while sum(int(game_desk_dict[item]) for item in game_desk_dict) > 0:
        game_desk_dict, shoot_results_dict = players_shot(game_desk_dict, shoot_results_dict)
    print('Поздравляю! Вы уничтожили все вражеские корабли!')
    print_desk(start_game_desk_dict)


def create_game_desk(desk_size):
    # '''Создаем игровое поле с размером стороны=desk_size заполненное "0" и храним его в словаре.'''
    coordinate_2 = 'АБВГДЕЖЗКИ'
    coordinate_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    fields_list = []
    for letter in coordinate_1[:desk_size]:
        for number in coordinate_2[:desk_size]:
            fields_list.append('{}{}'.format(letter, number))
    game_desk_dict = dict.fromkeys(fields_list, '0')
    return game_desk_dict, fields_list


def fill_up_game_desk_by_warships(game_desk_dict, qtty_of_warships, fields_list):
    # Cоздаем список list_of_ships_indexes и удаляем из него N=qtty_of_warships элементов с рандомным индексом.
    # Затем вносим вносим суда в игровое поле game_desk_dict
    import random
    list_of_ships_indexes = [ships for ships in range(0, abs(len(game_desk_dict)))]
    qtyy_of_empty_fields = abs(len(game_desk_dict)) - qtty_of_warships
    for i in range(0, qtyy_of_empty_fields):
        index = random.randint(0, len(list_of_ships_indexes)-1)
        list_of_ships_indexes.pop(index)
        i += 1
    for elem in list_of_ships_indexes:
        field_id = fields_list[elem]
        game_desk_dict[field_id] = '1'
    return game_desk_dict


def print_desk(game_desk_dict):
    # Функция выводит на экран полученное игровую доску
    str = ''
    for key in game_desk_dict:
        str += game_desk_dict[key]
    i = 0
    coordinate_1 = 1
    coordinate_2 = 'АБВГДЕЖЗКИ'
    string_with_spaces = '  '
    for chr in coordinate_2[:desk_size]:
        string_with_spaces = string_with_spaces + chr + ' '
    print(string_with_spaces)
    while i < len(str):
        string_with_spaces = '{} '.format(coordinate_1)
        for chr in str[i:i+desk_size]:
            string_with_spaces =  string_with_spaces + chr + ' '
        print(string_with_spaces)
        i += desk_size
        coordinate_1 += 1


def players_shot(game_desk_dict, shoot_results_dict):
    shot = input('Введите координаты для выстрела в формате (1А)')
    try:
        if game_desk_dict[shot] == '1':
            print('Вы подбили вражеский корабль!')
            game_desk_dict[shot] = '0'
            shoot_results_dict[shot] = 'W'
        else:
            print('Вы промахнулись')
            shoot_results_dict[shot] = 'X'
        print_desk(shoot_results_dict)
    except KeyError as error:
        print("Вы ввели ошибочные координаты для выстрела")
    return game_desk_dict, shoot_results_dict



start_game()

