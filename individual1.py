#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    wallpaper_price = float(input("Введите цену рулона обоев: "))
    paint_can_price = float(input("Введите цену банки краски: "))

    wallpaper_cost = 8 * wallpaper_price
    paint_cost = 2 * paint_can_price

    total_cost = wallpaper_cost + paint_cost

    discount = 0
    if 200 <= total_cost < 500:
        discount = 0.03
    elif 500 <= total_cost < 800:
        discount = 0.05
    elif 800 <= total_cost < 1000:
        discount = 0.07
    elif total_cost >= 1000:
        discount = 0.09

    final_amount = total_cost * (1 - discount)

    print(f"Покупатель заплатил {final_amount} рублей.")
