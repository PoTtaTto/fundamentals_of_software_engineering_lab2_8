#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def multiply_until_zero():
    """
    Считывает числа с клавиатуры и перемножает их до ввода 0.

    Возвращает произведение введенных чисел.
    """
    result = 1
    while True:
        num = int(input('Введите число (для остановки введите 0): '))
        if num == 0:
            break
        result *= num
    return result


if __name__ == '__main__':
    result = multiply_until_zero()
    print(f'Произведение введенных чисел: {result}')
