#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_input():
    """
    Запрашивает ввод с клавиатуры и возвращает полученную строку.

    Returns:
    - str: Введенная строка.
    """
    user_input = input("Введите значение: ")
    return user_input


def test_input(value):
    """
    Проверяет, можно ли значение преобразовать к целому числу.

    Args:
    - value (str): Значение для проверки.

    Returns:
    - bool: True, если значение можно преобразовать в int, иначе False.
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def str_to_int(value):
    """
    Преобразует переданное значение к целочисленному типу.

    Args:
    - value (str): Значение для преобразования.

    Returns:
    - int: Преобразованное целочисленное значение.
    """
    return int(value)


def print_int(number):
    """
    Выводит переданное значение на экран.

    Args:
    - number (int): Значение для вывода.
    """
    print(number)


if __name__ == '__main__':
    user_value = get_input()
    if test_input(user_value):
        int_value = str_to_int(user_value)
        print_int(int_value)
    else:
        print("Введенное значение нельзя преобразовать в целое число.")
