# Task 1
# У вас есть вложенный список чисел. НАпишите функцию генератор который вернет все элементы коллекции по очереди.

# import collections
#
# items = [1, 2, [3, 4, [5, 6], 7], 8]
#
# def flatten(l):
#     for el in l:
#         if isinstance(el, collections.Iterable):
#             for sub in flatten(el):
#                 yield sub
#         else:
#             yield el
#
# for elem in flatten(items):
#     print(elem)
#
#
#
# gen = flatten(items)
# next(gen)
# next(gen)
# print(next(gen))
# print(next(gen))
# next(gen)
# print(next(gen))
# next(gen)





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


# def start_game():
#     global desk_size
#     desk_size = int(input('Подалуйста введите размер игрового поля(цифра от 2 до 10)'))
#     qtty_of_warships = int(input('Пожалуйста введите количество кораблей '
#                                  'на поле(цифра от 1 до {})'.format(desk_size**2-1)))
#     if qtty_of_warships > desk_size**2 - 1:
#         qtty_of_warships = desk_size**2 - 1
#     game_desk_dict, fields_list = create_game_desk(desk_size)
#     # Под конец решил распечатать в конце игры начальное состояние доски(start_game_desk_dict), но столкнулся с
#     # проблемой. Не могу сделать отдельную копию словаря. Три способа перепробовал,а он все равно друг на game_desk_dict
#     #  ссылаются. Может какие-то настройки интепритатора...
#     start_game_desk_dict = {**game_desk_dict}
#     fill_up_game_desk_by_warships(game_desk_dict, qtty_of_warships, fields_list)
#     shoot_results_dict = create_game_desk(desk_size)[0]
#     while sum(int(game_desk_dict[item]) for item in game_desk_dict) > 0:
#         game_desk_dict, shoot_results_dict = players_shot(game_desk_dict, shoot_results_dict)
#     print('Поздравляю! Вы уничтожили все вражеские корабли!')
#     print_desk(start_game_desk_dict)
#
#
# def create_game_desk(desk_size):
#     # '''Создаем игровое поле с размером стороны=desk_size заполненное "0" и храним его в словаре.'''
#     coordinate_2 = 'АБВГДЕЖЗКИ'
#     coordinate_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     fields_list = []
#     for letter in coordinate_1[:desk_size]:
#         for number in coordinate_2[:desk_size]:
#             fields_list.append('{}{}'.format(letter, number))
#     game_desk_dict = dict.fromkeys(fields_list, '0')
#     return game_desk_dict, fields_list
#
#
# def fill_up_game_desk_by_warships(game_desk_dict, qtty_of_warships, fields_list):
#     # Cоздаем список list_of_ships_indexes и удаляем из него N=qtty_of_warships элементов с рандомным индексом.
#     # Затем вносим вносим суда в игровое поле game_desk_dict
#     import random
#     list_of_ships_indexes = [ships for ships in range(0, abs(len(game_desk_dict)))]
#     qtyy_of_empty_fields = abs(len(game_desk_dict)) - qtty_of_warships
#     for i in range(0, qtyy_of_empty_fields):
#         index = random.randint(0, len(list_of_ships_indexes)-1)
#         list_of_ships_indexes.pop(index)
#
#     for elem in list_of_ships_indexes:
#         field_id = fields_list[elem]
#         game_desk_dict[field_id] = '1'
#     return game_desk_dict
#
#
# def print_desk(game_desk_dict):
#     # Функция выводит на экран полученное игровую доску
#     str = ''
#     for key in game_desk_dict:
#         str += '{} '.format(game_desk_dict[key])
#     i = 0
#     coordinate_1 = 1
#     coordinate_2 = 'АБВГДЕЖЗКИ'
#     string_with_spaces = '  '
#     for chr in coordinate_2[:desk_size]:
#         string_with_spaces = string_with_spaces + chr + ' '
#     print(string_with_spaces)
#     while i < len(str):
#         string_with_spaces = '{} '.format(coordinate_1)
#         for chr in str[i:i+desk_size]:
#             string_with_spaces =  string_with_spaces + chr + ' '
#         print(string_with_spaces)
#         i += desk_size
#         coordinate_1 += 1
#
#
# def players_shot(game_desk_dict, shoot_results_dict):
#     shot = input('Введите координаты для выстрела в формате (1А)')
#     try:
#         if game_desk_dict[shot] == '1':
#             print('Вы подбили вражеский корабль!')
#             game_desk_dict[shot] = '0'
#             shoot_results_dict[shot] = 'W'
#         else:
#             print('Вы промахнулись')
#             shoot_results_dict[shot] = 'X'
#         print_desk(shoot_results_dict)
#     except KeyError as error:
#         print("Вы ввели ошибочные координаты для выстрела")
#     return game_desk_dict, shoot_results_dict
# #
#
#
# start_game()

# class WarshipBattle():
#     def __init__(self, ds=None, qw=None):
#         self.desk_size = ds
#         self.qtty_of_warships = qw

    #
    # def set_game_parameters(self):
    #     self.desk_size = int(input('Подалуйста введите размер игрового поля(цифра от 2 до 10)'))
    #     self.qtty_of_warships = int(input('Пожалуйста введите количество кораблей '
    #                                      'на поле(цифра от 1 до {})'.format(self.desk_size**2-1)))


    # def create_game_desk(self):
    #     import random
    #     self.coordinate_str = '  {}'. format(' А Б В Г Д Е Ж З К И'[:self.desk_size*2])
    #     self.game_desk_list = [[0] * self.desk_size] * self.desk_size
    #     # self.game_desk_list = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    #     self.shoot_results_list = [['O'] * self.desk_size] * self.desk_size

    # def players_shot(self):
    #     shot = input('Введите координаты для выстрела в формате (1А)')
    #     try:
    #         if self.game_desk_dict[shot] == '1':
    #             print('Вы подбили вражеский корабль!')
    #             self.game_desk_dict[shot] = '0'
    #             self.shoot_results_dict[shot] = 'W'
    #         else:
    #             print('Вы промахнулись')
    #             self.shoot_results_dict[shot] = 'X'
    #         self.print_desk(self.shoot_results_dict)
    #     except KeyError as error:
    #         print("Вы ввели ошибочные координаты для выстрела")



    # def desk_print(self, desk_list):
    #     print(self.coordinate_str)
    #     str_num = 1
    #     for row in desk_list:
    #         str_for_print = str(str_num) + '| '
    #         for field in row:
    #             str_for_print += str(field) + ' '
    #         print(str_for_print)
    #         str_num += 1

    # def game(self):
    #     self.set_game_parameters()
    #     self.create_game_desk()
    #     # self.print_desk(self.game_desk_dict)
    #     self.fill_up_game_desk_by_warships()
    #     print(s.__dict__)
    #     while sum(int(self.game_desk_dict[item]) for item in self.game_desk_dict) > 0:
    #         self.players_shot()
    #     print('Поздравляю! Вы уничтожили все вражеские корабли!')



# s = WarshipBattle(4,2)
#
# s.create_game_desk()
# s.desk_print(s.game_desk_list)
# s.desk_print(s.shoot_results_list)
# print(s.game_desk_list)


import random


class ShipBatle():
    def __init__(self, name=None):
        self.name = name
        self.stop_game = 0


    def create_game_desk(self, desk_size=None, qtty_of_ships_2=None, qtty_of_ships_1=None):
        self.desk_size = desk_size
        self.qtty_of_two_deck_ships = qtty_of_ships_2
        self.qtty_of_one_deck_ships = qtty_of_ships_1
        self.list_of_empty_fields = [x for x in range(0, desk_size**2)]
        self.desk = [[0]*desk_size for i in range(desk_size)]
        self.shoot_result = [['S'] * desk_size for i in range(desk_size)]
        self.decks_count = qtty_of_ships_1 + qtty_of_ships_2 * 2
        self.fill_desk()


    def fill_desk(self):
        while self.qtty_of_two_deck_ships > 0:
            first_deck = random.choice(self.list_of_empty_fields)
            second_deck = self.second_deck_choice(first_deck)
            border_list = self.make_border_lst([first_deck, second_deck])
            self.update_list_of_empy_fileds([first_deck, second_deck], border_list)
            self.qtty_of_two_deck_ships -= 1
        while self.qtty_of_one_deck_ships > 0:
            ship = random.choice(self.list_of_empty_fields)
            border_list = self.make_border_lst([ship])
            self.update_list_of_empy_fileds([ship], border_list)
            self.qtty_of_one_deck_ships -= 1


    def update_list_of_empy_fileds(self, ship, borders_lst):
        for desk in ship:
            idx_1 = desk // self.desk_size
            idx_2 = desk - self.desk_size * idx_1
            self.desk[idx_1][idx_2] = 1
            self.list_of_empty_fields.remove(desk)
        for border_field in borders_lst:
            if border_field in self.list_of_empty_fields:
                self.list_of_empty_fields.remove(border_field)
            else:
                pass


    def second_deck_choice(self, first_deck):
        if first_deck % (self.desk_size - 1) == 0:
            list_of_possible_fileds_for_second_deck = [first_deck - self.desk_size, first_deck - 1,
                                                       first_deck + self.desk_size]
        if first_deck % (self.desk_size) == 0:
            list_of_possible_fileds_for_second_deck = [first_deck - self.desk_size, first_deck + 1,
                                                       first_deck + self.desk_size]
        else:
            list_of_possible_fileds_for_second_deck = [first_deck - self.desk_size, first_deck - 1, first_deck + 1,
                                                       first_deck + self.desk_size]
        list_of_possible_fileds_for_second_deck = self.exclude_incorrect_and_occupied_fields(
                                                        list_of_possible_fileds_for_second_deck)
        second_deck = random.choice(list_of_possible_fileds_for_second_deck)
        return second_deck


    def exclude_incorrect_and_occupied_fields(self, list_of_possible_fields_for_second_deck):
        result_lst = []
        for field in list_of_possible_fields_for_second_deck:
            if field > 0 and field < self.desk_size ** 2 and field in self.list_of_empty_fields:
                result_lst.append(field)
        return result_lst


    def make_border_lst(self, lst):
        if len(lst) > 1:
            result_lst = [lst[0] - self.desk_size, lst[0] - 1, lst[0] + 1, lst[0] + self.desk_size, lst[0] - self.desk_size - 1,
                          lst[0] - self.desk_size + 1, lst[0] + self.desk_size - 1, lst[0] + self.desk_size + 1]
            resul_lst_2 = [lst[1] - self.desk_size, lst[1] - 1, lst[1] + 1, lst[1] + self.desk_size, lst[1] - self.desk_size - 1,
                           lst[1] - self.desk_size + 1, lst[1] + self.desk_size - 1, lst[1] + self.desk_size + 1]
            for field in resul_lst_2:
                result_lst.append(field)
            for field in lst:
                result_lst.remove(field)
        else:
            result_lst = [lst[0] - self.desk_size, lst[0] - 1, lst[0] + 1, lst[0] + self.desk_size, lst[0] - self.desk_size - 1,
                          lst[0] - self.desk_size + 1, lst[0] + self.desk_size - 1, lst[0] + self.desk_size + 1]
        return list(set(result_lst))


    def game(self):
        self.desk_size = int(input('По;алуйста введите размер игрового поля(цифра от 4 до 10)'))
        self.qtty_of_two_deck_ships = int(input('Пожалуйста введите количество двух-палубных короблей(цифра от 1 до '
                                                '{})'.format(self.desk_size // 2)))
        self.qtty_of_one_deck_ships = int(input('Пожалуйста введите количество двух-палубных короблей(цифра от 1 до '
                                                '{})'.format(self.desk_size // 2)))
        player_1 = ShipBatle('Player 1')
        player_2 = ShipBatle('Player 2')
        player_1.create_game_desk(self.desk_size, self.qtty_of_two_deck_ships, self.qtty_of_one_deck_ships)
        player_2.create_game_desk(self.desk_size, self.qtty_of_two_deck_ships, self.qtty_of_one_deck_ships)
        players_list = [player_1, player_2]
        while self.stop_game == 0:
            for player in players_list:
                print(player.__dict__)
                if self.stop_game == 0:
                    self.players_shot(player)
        print("Game over")


    def prity_print(self, lst):
        coordinate_2 = 'АБВГДЕЖЗКИ'
        str_to_print = ''
        for i in range(0, self.desk_size):
            str_to_print = str_to_print + coordinate_2[i] + '    '
        print('    {}'.format(str_to_print))
        i = 1
        for row in lst:
            print('{} {}'.format(i,row))
            i += 1


    def players_shot(self, player):
        coordinate_2 = 'АБВГДЕЖЗКИ'
        hit = 1
        try:
            while hit == 1:
                self.prity_print(player.shoot_result)
                shot = input('{} ведите координаты для выстрела в формате (1А)'.format(player.name))
                idx_1 = int(shot[0])-1
                idx_2 = coordinate_2.index(shot[1])
                if player.desk[idx_1][idx_2] == 1:
                    print('Вы попали во вражеский корабль!')
                    player.desk[idx_1][idx_2] = '0'
                    player.shoot_result[idx_1][idx_2] = 'W'
                    player.decks_count -= 1
                    self.prity_print(player.shoot_result)
                    if player.decks_count == 0:
                        self.stop_game = 1
                        hit = 0
                if player.desk[idx_1][idx_2] == 0 or player.desk[idx_1][idx_2] == 'W':
                    print('Вы промахнулись')
                    player.shoot_result[idx_1][idx_2] = 'X'
                    self.prity_print(player.shoot_result)
                    hit = 0
        except Exception as error:
            print("Мимо! В следующий раз делайте выстрел в границах игрового поля", error)


game = ShipBatle()

game.game()