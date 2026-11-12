def perimeter_area(a,b):

    perimeter = 2*a+2*b  # Расчёт периметра
    area = a*b  # Расчёт площади

    return perimeter, area
if __name__ == "__main__":
    perimeter, area = perimeter_area(5,7)
    print(perimeter, area)