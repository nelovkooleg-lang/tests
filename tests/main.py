def square_params(a):

    perimeter = 4 * a  # Расчёт периметра
    area = a ** 2  # Расчёт площади

    return perimeter, area
if __name__ == "__main__":
    perimeter, area = square_params(6)
    print(perimeter, area)
