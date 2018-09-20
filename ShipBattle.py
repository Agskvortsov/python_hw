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
        except ValueError as error:
            print("Мимо! В следующий раз делайте выстрел в границах игрового поля")


game = ShipBatle()

game.game()