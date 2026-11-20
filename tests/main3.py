def circle_area(r):

    P = 3.14  # число «Пи»
    circle_length = 2 * P * r  # Расчёт длины окружности
    area = P * r ** 2  # Расчёт площади круга

    return area, circle_length
if __name__ == '__main__':
    area, circle_length = circle_area(6)
    print(area, circle_length)
