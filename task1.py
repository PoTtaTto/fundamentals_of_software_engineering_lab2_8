#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def test():
    """Проверяет ввод пользователя на положительное или отрицательное число."""
    num = int(input('Введите целое число: '))
    if num > 0:
        positive()
    elif num < 0:
        negative()


def positive():
    """Выводит сообщение 'Положительное'."""
    print('Положительное')


def negative():
    """Выводит сообщение 'Отрицательное'."""
    print('Отрицательное')


if __name__ == '__main__':
    test()
