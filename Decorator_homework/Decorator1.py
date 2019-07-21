#декоратор, подсчитывающий время выполнения функции


import datetime

def input_func(func):
    def time_counter(*args):
        start_to_run = datetime.datetime.now()
        func(*args)
        end_of_run = datetime.datetime.now()
        diff = end_of_run - start_to_run
        print("Время расчета функции = " + str(diff))
    return time_counter


@input_func
def any_func_to_count(a, b, c, d):
    result = (a * b / c / d) ** 2
    for l in range(1, int(result)):
        result = l + result
    print (result)



#Чекаем работу
any_func_to_count(10, 55555, 6599.44, 0.1568848)