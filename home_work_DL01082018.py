# Задача-1
#
# Написать свой lru_cache  декоратор с аргументом. В качестве аргумента он будет принимать maxsize-
# максимальный размер кеша.

def cach_decorator(func, max_size=4):
    """Variant 1. В кеш попадают первые max_size*аргументов"""
    results = {}
    def wrapper(arg):

        if arg in results.keys():
            results[arg][1] += 1
            print( 'Used cache with result {}'.format(results.get(arg)[0]))
        else:
            if len(results) < max_size:
                results[arg] = [func(arg), 1]
                print( 'Function executed with function result1 = {}'.format(func(arg)))
            else:
                print('Function executed with function result2 = {}'.format(func(arg)))
        print(results)
    return wrapper


def cach_decorator(func, max_size=3):
    """Variant 1. Кеш обновляется каждые max_size*2 уникальных аргумента. Кеш сортируется по количеству обращений и
    половина которая набрала больше всего "обращений" остается, а вторая половина выбрасывается. При этом счетчики
    обращений у оставшихся элементов обнуляются, что при следующей сортировке и обновлении даст возможность новым
    аргументам остаться в кеше"""
    results = dict()
    def wrapper(arg):
        if arg in results.keys():
            results[arg][1] += 1
            print( 'Used cache with result {}'.format(results.get(arg)[0]))
        else:
            if len(results) < max_size*2:
                results[arg] = [func(arg), 1]
                print( 'Function executed with function result1 = {}'.format(func(arg)))
            else:
                print('Function executed with function result2 = {}'.format(func(arg)))
                s = list(sorted(results.items(), key=lambda x: x[1][1], reverse=True))[0:max_size]
                results.clear()
                for elem in s:
                    results[elem[0]] = list([elem[1][0],0])

    return wrapper



@cach_decorator
def my_func(a):
        return a*10

my_func(1)
my_func(5)
my_func(10)
my_func(1)
my_func(2)
my_func(1)
my_func(20)
my_func(5)


#
# Задача-2
#
# Написать свой декоратор который будет проверять остаток от деления числа 100 на результат работы функции ниже.
# Если остаток от деления = 0, вывести сообщение "We are OK!», иначе «Bad news guys, we got {}» остаток от деления.


def decorator(func_to_decorate):
    def wrapper(arg):
        number = func_to_decorate(arg)
        print(number, 100%number)
        if 100%number == 0:
            return "we are ok"
        else:
            return "Bad news guys, we got {}".format(100%number)
    return wrapper

@decorator
def my_func(a):
        return a * 10


print(my_func(11))


# Здача-4
#
# Написать декоратор который будет кешировать значения аргументов и результаты работы вашей функции и записывать его в
# переменную cache. Если аргумента нет в переменной cache и функция выполняется, вывести сообщение «Function executed with
#     counter = {}, function result = {}» и количество раз сколько эта функция выполнялась. Если значение берется из
#     переменной cache, вывести сообщение «Used cache with counter = {}» и количество раз обращений в cache.

def cach_counter(func):
    results = {'counter':0}
    def wrapper(arg):
        results['counter'] += 1
        if arg in results.keys():
            results[arg][1] += 1
            print( 'Used cache with counter = {} and result {}'.format(results.get('counter'), results.get(arg)[0]))
        else:
            result = func(arg)
            results[arg] = [result, 1]
            print( 'Function executed with counter = {}, function result = {}'.format(results.get('counter'), result))
        print(results)

    return wrapper


@cach_counter
def my_func(a):
        return 10*a

my_func(1)
my_func(5)
my_func(10)
my_func(1)
my_func(2)
my_func(1)
my_func(20)
my_func(5)