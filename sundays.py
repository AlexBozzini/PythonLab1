def get_sunday_count():
    sunday_count = 0
    for i in range(1901, 2000):
        for j in range(1, 12):
            for k in range(1, get_number_of_days(j, i)):
                if j == 2000:
                    c = 20
                else:
                    c = 19
                f = k + ((13 * j - 1) / 5) + ((i - 1900) / 4) + (c / 4) - 2 * c
                if f % 7 == 0:
                    sunday_count = sunday_count + 1
        print(sunday_count)
        return sunday_count


def get_number_of_days(month, year):
    global number_of_days
    if month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
        number_of_days = 31
    elif month == 2:
        if year % 100 == 0 and year % 400 != 0:
            number_of_days = 28
        elif year % 400 == 0:
            number_of_days = 29
        elif year % 100 != 0 and year % 4 == 0:
            number_of_days = 29
        elif year % 100 != 0 and year % 4 != 0:
            number_of_days = 28
    else:
        number_of_days = 30
    return number_of_days


get_sunday_count()
