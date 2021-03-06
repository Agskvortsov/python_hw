# # Задача-1
# # У вас есть список(list) IP адрессов. Вам необходимо создать
# # класс который будет иметь методы:
# # 1) Получить список IP адресов
# # 2) Получить список IP адресов в развернутом виде
# # (10.11.12.13 -> 13.12.11.10)
# # 3) Получить список IP адресов без первых октетов
# # (10.11.12.13 -> 11.12.13)
# # 4) Получить список последних октетов IP адресов
# # (10.11.12.13 -> 13)
#
#
# class IpAdressOps():
#     def __init__(self, adr_lst):
#         self.ip_list = adr_lst
#
#     def get_revese_address(self):
#         reversed_list = []
#         for elem in self.ip_list:
#             reversed_ip =  '{3}.{2}.{1}.{0}'.format(*elem.split('.'))
#             reversed_list.append(reversed_ip)
#         return reversed_list
#
#     def get_ip_without_first_octet(self):
#         revised_address = []
#         for elem in self.ip_list:
#             reversed_ip = '{1}.{2}.{3}'.format(*elem.split('.'))
#             revised_address.append(reversed_ip)
#         return revised_address
#
#     def get_last_octet(self):
#         forth_octets_list = []
#         for elem in self.ip_list:
#             reversed_ip = '{3}'.format(*elem.split('.'))
#             forth_octets_list.append(reversed_ip)
#         return forth_octets_list
#
# list = ['192.168.0.1', '192.166.0.4', '160.164.0.3', '192.168.0.2']
# adrlist = IpAdressOps(list)
# print(list)
# print(adrlist.get_revese_address())
# print(adrlist.get_ip_without_first_octet())
# print(adrlist.get_last_octet())
#
# # Задача-2
# # У вас несколько JSON файлов. В каждом из этих файлов есть
# # произвольная структура данных. Вам необходимо написать
# # класс который будет описывать работу с этими файлами, а
# # именно:
# # 1) Запись в файл
# # 2) Чтение из файла
# # 3) Объединение данных из файлов в новый файл
# # 4) Получить путь относительный путь к файлу
# # 5) Получить абсолютный путь к файлу
# import json
# import os.path
#
# class JsonFile():
#     def __init__(self, path_file):
#         self.path_to_file = path_file
#
#     def read_file(self):
#         with open(self.path_to_file, 'r') as file:
#             data = json.load(file)
#         return data
#
#     def write_to_file(self, file_dest):
#         with open(file_dest, 'w') as file_dest:
#             file_dest.writelines(json.dumps(self.read_file(), separators=(',', ':')))
#
#     def unite_files(self, obj_2, path_to_united_file):
#         data1 = self.read_file()
#         with open(obj_2.path_to_file, 'r') as file:
#             data2 = json.load(file)
#         united_data = {'file1':data1, 'file_2' :data2}
#         with open(path_to_united_file, 'w') as file:
#             file.writelines(json.dumps(united_data, separators=(',', ':')))
#         return JsonFile(path_to_united_file)
#
#     def get_absolute_path(self):
#         return os.path.dirname(self.path_to_file)
#
#     def qet_relative_path(self):
#         return '/'.join(os.path.relpath(self.path_to_file).split('/')[:-1])
#
#
#
# file1 = JsonFile('/Users/alexskvortsov/PycharmProjects/python_hw/new_dir1/one_more_dir/json_file_1.json')
# file2 = JsonFile('/Users/alexskvortsov/PycharmProjects/python_hw/data_file.json')
#
# file3 = file1.unite_files(file2, '/Users/alexskvortsov/PycharmProjects/python_hw/united_file.json')
#
# print(file3.read_file())
# print(os.path.dirname(file3.path_to_file))
# print(file1.get_absolute_path())
# print(file1.qet_relative_path())
#
#
# # Задача-3
# #
# # Создайте класс который будет хранить параметры для
# # подключения к физическому юниту(например switch). В своем
# # списке атрибутов он должен иметь минимальный набор
# # (unit_name, mac_address, ip_address, login, password).
# # Вы должны описать каждый из этих атрибутов в виде гетеров и
# # сеттеров(@property). У вас должна быть возможность
# # получения и назначения этих атрибутов в классе.
#
#
# class ConntectionData():
#
#     def __init__(self, unite_name=None, mac_address=None, ip_address=None, login=None, password=None):
#         self._unite_name = unite_name
#         self._mac_address = mac_address
#         self._ip_address = ip_address
#         self._login = login
#         self._password = password
#
#     @property
#     def unite_name(self):
#         return self._unite_name
#
#     @unite_name.setter
#     def unite_name(self, volume):
#         self._unite_name = volume
#
#     @property
#     def mac_address(self):
#         return self._mac_address
#
#     @mac_address.setter
#     def mac_address(self, volume):
#         self._mac_address = volume
#
#
#     @property
#     def ip_address(self):
#         return self._ip_address
#
#     @ip_address.setter
#     def ip_address(self, volume):
#         self._ip_address = volume
#
#     @property
#     def login(self):
#         return self._login
#
#     @login.setter
#     def login(self, volume):
#         self._login = volume
#
#     @property
#     def password(self):
#         return self._password
#
#     @password.setter
#     def password(self, volume):
#         self._password = volume
#
#     def __str__(self):
#         return str(self.__dict__)
#
# f = ConntectionData('unite_one', '00:26:57:00:1f:02', '234.234.345.123', 'SASHA', 'WEF3423ed' )
# print(f.unite_name)
# f.unite_name ='cdsc'
# print(f.unite_name)
# print(f.login)
#
# # Задача-4
# # Для решения этой задачи вам необходимо будет познакомиться
# # с форматом данных YAML(YML). Для работы с этим типом данных
# # так же существуют библиотеки на Python (например PyYAML).
# #
# # Создайте класс который будет помогать вам в решении повседневных задач а именно:
# # 1)Запись в файл
# # 2)Чтение из файла
#
#
# import yaml
# import io
#
# # Define data
# data = {'a list': [1, 42, 3.141, 1337, 'help', u'€'], 'a string': 'bla',
#         'another dict': {'foo': 'bar',
#                          'key': 'value',
#                          'the answer': 42}}
#
# class YamlOperate():
#     def __init__(self, data=None):
#         self.data = data
#
#     def read_from_file(self, filename):
#         with io.open(filename, 'r', encoding='utf-8') as stream:
#             data_loaded = yaml.load(stream)
#         self.data = data_loaded
#
#     def write_to_file(self, filename):
#         with io.open('data.yaml', 'w', encoding='utf-8') as outfile:
#             yaml.dump(self.data, outfile, default_flow_style=False, allow_unicode=True)
#
#
# f = YamlOperate(data)
# print(f)
# print(f.data)
# f.write_to_file('data.yaml')
# d = YamlOperate()
# print('d', d.data)
# d.read_from_file('data.yaml')
# print('d', d.data)

# *Задача - 5*
# ```Создать класс для представления информации о времени. Ваш класс должен иметь  возможности установки времени и
# изменения его отдельных полей (час, минута, секунда) с проверкой допустимости вводимых значений. В случае недопустимых
# значений полей выбрасываются исключения. Создать методы изменения времени на заданное количество часов, минут и
# секунд.```

class Time():
    def __init__(self):
        self._hours = 0
        self._minutes = 0
        self._seconds = 0


    @property
    def get_time(self):
        return 'Time is {} hours {} minutes and {} seconds'.format(self._hours, self._minutes, self._seconds)


    @get_time.setter
    def hours(self, hours):
        if int(hours) in range(1,25):
            self._hours = hours
        else:
            print('Hours value is incorrect')


    @get_time.setter
    def minutes(self, minutes):
        if int(minutes) in range(0,60):
            self._minutes = minutes
        else:
            print('Minutes value is incorrect')


    @get_time.setter
    def seconds(self, seconds):
        if int(seconds) in range(0,60):
            self._seconds = seconds
        else:
            print('Hours value is incorrect')


    def set_time(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds


    def change_time(self, hours=0, minutes=0, seconds=0):
        self._seconds += int(seconds)
        if self._seconds > 60:
            self._seconds = self._seconds - 60
            self._minutes += 1

        self._minutes += int(minutes)
        if self._minutes > 60:
            self._minutes = self._minutes - 60
            self._hours += 1

        self._hours += int(hours)
        if self._hours > 24:
            self._hours = self._hours - 24


t = Time()
print(t.get_time)
t.set_time(12, 50, 50)

print(t.get_time)
t.change_time(24, 10, 58)

print(t.get_time)

f = Time()
f.hours = 25
print(f.get_time)

# Задача - 6
# Создайте класс Student, который содержит атрибуты: фамилия и инициалы, номер группы, успеваемость (массив из пяти
# элементов). Создать массив(студентов) из десяти элементов такого типа, упорядочить записи по возрастанию среднего балла.
# Добавить возможность вывода фамилий и номеров групп студентов, имеющих оценки, равные только 4 или 5.

class Student():
    def __init__(self, name, initials, group_no, marks):
        self.name = name
        self.initials = initials
        self.group_number = group_no
        self.marks = marks


    def __str__(self):
        return str(self.__dict__)


def aver_mark(stud):
    return sum(stud.marks)/len(stud.marks)


def sort_by_average_mark(stud_lst):
    return sorted(stud_lst, key=aver_mark)


def list_of_students_print(lst):
    for stud in lst:
        print(stud)


def selection_stud_print_by_average_marks(lst, marks_level):
    for stud in lst:
        if aver_mark(stud) > marks_level:
            print(stud, aver_mark(stud))

def selection_stud_print_by_marks(lst, marks):
    marks_lst_to_declain = [1,2,3,4,5]
    for mark in marks:
        marks_lst_to_declain.remove(mark)
    for stud in lst:
        for mark in marks_lst_to_declain:
            if mark in stud.marks:
                break
        else:
            print(stud)







a = Student("aaaaaa", "A.G.", "4", [5,5,5,5,5])
b = Student("bbbbbbb", "A.G.", "4", [1,1,1,2,2])
c = Student("Skvortsov", "A.G.", "4", [4,4,5,4,5])
d = Student("ddddddd", "A.G.", "4", [5,4,2,3,5])
e = Student("Eeeeeeee", "A.G.", "4", [4,4,2,3,5])
f = Student("fffffff", "A.G.", "4", [3,5,2,3,5])
g = Student("ggggggg", "A.G.", "4", [3,2,2,3,5])
h = Student("hhhhhh", "A.G.", "4", [3,1,2,3,5])
i = Student("i", "A.G.", "4", [3,4,2,2,3])
j = Student("jjjjjj", "A.G.", "4", [5,4,5,3,5])

stud_list = [a,b,c,d,e,f,g,h,i]


sorted_stud = sort_by_average_mark(stud_list)
list_of_students_print(sorted_stud)
selection_stud_print_by_average_marks(stud_list, 4)
selection_stud_print_by_marks(stud_list, [4,5])

