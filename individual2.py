#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


if __name__ == '__main__':
    x1 = float(input("Введите x-координату центра первой окружности: "))
    y1 = float(input("Введите y-координату центра первой окружности: "))
    r1 = float(input("Введите радиус первой окружности: "))

    x2 = float(input("Введите x-координату центра второй окружности: "))
    y2 = float(input("Введите y-координату центра второй окружности: "))
    r2 = float(input("Введите радиус второй окружности: "))

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    if distance > r1 + r2:
        print("Окружности не пересекаются")
    elif distance < abs(r1 - r2):
        print("Одна окружность внутри другой, бесконечно много пересечений")
    elif distance == 0 and r1 == r2:
        print("Окружности совпадают, бесконечно много пересечений")
    else:
        alpha = math.acos((r1 ** 2 + distance ** 2 - r2 ** 2) / (2 * r1 * distance))
        beta = math.atan2((y2 - y1), (x2 - x1))

        intersection_point1 = (x1 + r1 * math.cos(beta + alpha), y1 + r1 * math.sin(beta + alpha))
        intersection_point2 = (x1 + r1 * math.cos(beta - alpha), y1 + r1 * math.sin(beta - alpha))

        if intersection_point1 == intersection_point2:
            print("Окружности касаются в одной точке")
        else:
            print(f"Окружности пересекаются в двух точках: {intersection_point1}, {intersection_point2}")
