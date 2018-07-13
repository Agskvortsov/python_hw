# 1) Сгенерировать dict() из списка ключей ниже по формуле
# (key : key* key). keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def dict_generator(keys):
    dict={}
    for key in keys:
       dict[key] = key * key
    return dict

print(dict_generator(keys))


# 2)Сгенерировать массив(list()). Из диапазона чисел от 0 до 100 записать в
# результирующий массив только четные числа.

def list_generator(fm, to):
    pre_list = [elem for elem in range(fm, to)]
    even_list = [elem for elem in pre_list if elem%2==0]
    return even_list

print(list_generator(1,101))



# 3) Заменить в произвольной строке согласные буквы на гласные.

import random

def replacing_by_vowel(str):
    str_vowel = "AEIOUaeiou"
    for letter in str:
        if letter in "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz":
            i=random.randint(0,9)
            str = str.replace(letter, str_vowel[i])
    return str

print(replacing_of_vowel("ackfkJHduKRP"))


# 4) Дан массив чисел. [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]  
# 4.1) убрать из него повторяющиеся элементы 

lst = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 96, 2, 32, 76, 3, 10, 0, 1]

def replacing_of_repited(lst):
    lst_repl = set(lst)
    lst_new = []
    for elem in lst_repl:
        lst_new.append(elem)
    return lst_new

print(replacing_of_repited(lst))


# # 4.2) вывести 3 наибольших числа из исходного массива  

def print_highest_elem(lst, num_of_elem=3):
    lst_temp = replacing_of_repited(lst)
    lst_temp.sort()
    result_lst = []
    for i in range(len(lst_temp)-num_of_elem, len(lst_temp)):
        result_lst.append(lst_temp[i])
    return result_lst

# print(print_highest_elem(lst))


# # 4.3) вывести индекс минимального элемента массива 


def print_lowest_lst_elem(lst):
    max_elem = print_highest_elem(lst, 1)
    min_elem = max_elem[0]
    i = 0
    min_elem_index = 0
    for elem in lst:
        if elem < min_elem:
            min_elem_index = i
            min_elem = elem
        i += 1
    return min_elem_index

# print(print_lowest_lst_elem(lst))


# # 4.4) вывести исходный массив в обратном порядке

def reversing_lst(lst):
    lst.reverse()
    return lst

print(reversing_lst(lst))


# 5) Найти общие ключи в двух словарях 

dict_one = { 'a': 1,
             'b': 2,
            'c': 3,
            'd': 4 }

dict_two = {'a': 6,
            'b': 7,
            'z': 20,
            'x': 40}

def find_same_key(dic1, dic2):
    dict1_keys=[]
    same_key_lst = []
    for key in dic1:
        dict1_keys.append(key)
    for key in dic2:
        if key in dict1_keys:
            same_key_lst.append(key)
    return same_key_lst


print(find_same_key(dict_one, dict_two))


# 6.1) отсортировать массив из словарей по значению ключа ‘age'
data = [{'name': 'Viktor', 'city': 'Kiev', 'age': 30 },
        {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
        {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
        {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
        {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
        {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]

def sort_list_of_dict_by_key(lst, dict_key):
    new_dict = sorted(lst, key=lambda k: k[dict_key])
    return new_dict

def prety_print(lst):
    for elem in lst:
        print(elem)

prety_print(sort_list_of_dict_by_key(data,'age'))


# 6.2) сгруппировать данные по значению ключа 'city'        вывод должен быть такого вида :
#  {‘Kiev’: [ {‘name’: ‘Viktor’, ‘age’: 30 }, {‘name’: ‘Andrey’, ‘age’: 34}],
# ‘Dnepr’: [ {‘name’: ‘Maksim’, ‘age’: 20 }, {‘name’: ‘Artem’, ‘age’: 50}], 
# ‘Lviv’: [ {‘name’: ‘Vladimir’, ‘age’: 32 },  {‘name’: ‘Dmitriy’, ‘age’: 21}]        } 

def list_by_cities(lst):
    city_lst = []
    for elem in lst:
        if elem['city'] not in city_lst:
            city_lst.append(elem['city'])
    dict_by_cities = {}
    for city in city_lst:
        dict_by_cities[city] = []
        for elem in lst:
            if elem['city'] == city:
                name_age = {'name': elem['name'], 'age': elem['age'] }
                dict_by_cities[city].append(name_age)
    for city in dict_by_cities:
        print(city, dict_by_cities[city])
    return dict_by_cities

print(list_by_cities(data))





