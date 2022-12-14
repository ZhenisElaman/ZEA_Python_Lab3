#!/usr/bin/env python3
# coding=utf-8

# Имеется двумерный массив 4x5. Реализовать возможность заполнения его
# случайными числами. Реализовать команду выполнить задание, которая выполняет:
# Если во втором столбце стоят две единицы, то уменьшить макс. элемент первой
# строки в два раза, а все единицы в таблице заменить нулями.

import random  # импортируем модуль random для генерации случайных чисел


# Функция генерирует nxm массив случайных чисел до max_value, у которого
# стандартное значение 20
def random_array(n, m, max_value=20):
    array = []  # инициализируем массив
    # Цикл for. Оператор range выдает диапазон чисел, в данном случае
    # от 0 до n-1
    for i in range(0, n):
        sub_array = []  # инициализируем подмассив
        # Если передать range один аргумент, то нижняя граница 0, в данном
        # случае диапазон чисел будет от 0 до m-1
        for j in range(m):
            # Генерируем слуйчаное число от 0 до 19 и добавляем его в подмассив
            number = random.randint(0, max_value)
            sub_array.append(number)
        # Добавляем полученный подмассив в основной массив
        array.append(sub_array)
    return array  # возвращаем массив из случайных чисел


def print_array(array):  # функция выводит массив в удобочитаемой форме
    print()  # переход на новую строку
    # Циклу for также можно давать массивы, тогда перебирается каждый элемент
    for i in array:
        # Так как массив состоит из подмассивов, тогда каждый элемент тоже
        # можно перебрать используя цикл for
        for j in i:
            print("%d\t" % j, end='')  # выводим каждое значение и табуляцию
        print()  # переход на новую строку

def main():
    array = random_array(4, 5)  # заполняем массив случайными числами
    print_array(array)  # выводим массив на экран
    while True:
        key = int(input('Пересоздать массив? (1 - ДА/ 2 - Нет): '))
        if key == 1:
            array = random_array(4, 5)
            print_array(array)
        elif key == 2:
            a_max = 0
            for i in array: # перебираем строку
                if a_max < i[1]:
                    a_max = i[1]
                    rep = 1
                    row_max = i
                elif a_max == i[1]:
                    rep += 1
            print('Максимальный элемент 2 строки =', a_max)
            if rep > 1: # Если MAX-ов больше 1
                print('Во 2 строке не 1 максимальный элемент!')
            zero_rep = array[1].count(0) # Считаем НУЛИ во 2 строке
            print('Количество 0 во 2 строке =', zero_rep)
            key = int(input('Заменить максимальный элемент массива на количество 0 во 2 строке? (1 - ДА/ 2 - Нет): '))
            if key == 1:
                row_max[1] = zero_rep
                print_array(array)
                break
            else:
                break
        else:
            exit()


if __name__ == '__main__':
    main()