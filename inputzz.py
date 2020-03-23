from datetime import date
from getpass import getpass


def get_date():
    year_text = input("year: ")
    year = int(year_text)
    if year <= 3000:
        pass
    else:
        raise ValueError("max year 3000")
    month_text = input("month [1-12]: ")
    month = int(month_text)
    if 1 <= month <= 12:
        pass
    else:
        raise ValueError("month of range 1-12")
    day_text = input("day [1-31]: ")
    day = int(day_text)
    if 1 <= day <= 31:
        pass
    else:
        raise ValueError("day of range 1-31")
    result = date(year, month, day)
    print(result)


get_date()
