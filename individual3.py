#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    payment = int(input("Введите сумму, которую отдаёт покупатель: "))

    available_notes = [500, 100, 10, 5, 2, 1]

    print("Покупатель отдаст следующее количество купюр разного достоинства:")

    for note in available_notes:
        if payment >= note:
            count = payment // note
            payment %= note
            print(f"{note} р.: {count} шт.")
