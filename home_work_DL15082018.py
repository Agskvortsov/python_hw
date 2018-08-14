# *Задача-1*
# Познакомьтесь с модулем logging. Напишите функцию инициализации логгера. Используйте логгирование во всех задания ниже.
# Определите файл в который будет писать ваш логгер. Внимательно следите за уровнями логгирования.

list = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('a')]

import logging

logging.basicConfig(level = logging.INFO, filename = 'mylog.log', format="%(asctime)s:%(levelname)s:%(message)s")


def exclude_empty_tuple(lst):
    lst2 = []
    for elem in lst:
        for letter in elem:
            if letter.isalpha() == True:
                lst2.append(elem)
                logging.info('Loop. Elem = {}, Letter = {}'.format(elem, letter))
                break

    print(lst2)
    return lst2



exclude_empty_tuple(list)


# *Задача-2*
#
# У вас есть 2 файла. В каждом файле произвольные символы(строки). Ваша задача обьединить эти строки, преобразовать их в
# поток байт и записать поток байт в файл 3 с именем «Result.bin»

import logging

logging.basicConfig(level = logging.INFO, filename = 'mylogTusk2.log', format="%(asctime)s:%(levelname)s:%(message)s")


def file_to_list(file_mame):
    f = open(file_mame)
    lines_file = []
    for line in f:
        lines_file.append(line.strip())
    logging.info('List "{}" saved to file {}'.format(lines_file, file_mame))
    return lines_file

def two_lists_to_str(lst1, lst2):
    united_str = ''
    if len(lst1) >= len(lst2):
        i = 0
        while i < len(lst2):
            united_str += lst1[i] + lst2[i]
            i += 1
        while i < len(lst1):
            united_str += lst1[i]
            i += 1
    else:
        i = 0
        while i < len(lst1):
            united_str += lst1[i] + lst2[i]
            i += 1
        while i < len(lst2):
            united_str += lst2[i]
            i += 1
    logging.info('United string "{}" created'.format(united_str))
    return united_str

def str_to_bin_file(str, file_name):
    results = open(file_name, 'wb')
    results.write(str.encode())
    results.close()
    logging.info('Binary file "{}" '.format(file_name))

str_to_bin_file(two_lists_to_str(file_to_list('file1.txt'), file_to_list('file2.txt')), 'result.bin')

# *Задача-3*
#
# У вас есть файл. Ваша функция на вход принимает путь к этому файлу. Вам необходимо определить имя файла, название
# каталога и абсолютный путь. Внутри функции выполните все возможные проверки.```

import logging
import re
import os

logging.basicConfig(level = logging.INFO, filename = 'mylogTusk3.log', format="%(asctime)s:%(levelname)s:%(message)s")

def find_path_and_file_name(path_file_name):
    logging.info('Call function with path file name {} '.format(path_file_name))
    absolute_path = os.path.abspath(path_file_name)
    split_path = re.split(r'\/', absolute_path)
    logging.info('Splited path is {}'.format(split_path))
    file_directorie = split_path[-2]
    file_name = split_path[-1]
    logging.info('Abs path is {}, file deric is {}, file name is {}'.format(absolute_path, file_directorie, file_name))
    return absolute_path, file_directorie, file_name

find_path_and_file_name('python_hw/result.bin')
#
# *Задача-4*
#
# У вас есть строка вида «Name: Peter, Age: 20, Country: USA». Вам необходимо преобразовать эти данные и записать их в
# файл result.json,

import json

def string_to_json(str):
    str_as_dict = {}
    for elem in str.split(','):
        str_as_dict[elem.split(':')[0].strip()] = elem.split(':')[1].strip()
    return str_as_dict


def data_to_json(str):
    dict = string_to_json(str)
    with open("data_file.json", "w") as write_file:
        write_file.writelines(json.dumps(dict, separators=(',', ':')))

f = data_to_json(' Name    : Peter, Age: 20, Country: USA ')



data_to_json(' Name: Peter, Age: 20, Country: USA ')

# *Задача-5*
#
# Напишите функцию копирования файлов и каталогов. На вход ваша функция принимает два аргумента:
# -  путь файла или каталога который необходимо скопировать
# - путь каталога куда этот файл необходимо скопировать

import shutil


def copy_file(src, dst):
    shutil.copy(src, dst, follow_symlinks = True)



copy_file('mylog.log', 'mydir/new_dir1/one_more_dir')
