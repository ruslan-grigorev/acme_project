from datetime import date

def calculate_birthday_countdown(birthday):
    today = date.today()
    this_year_birthday = get_birthday_for_year(birthday, today.year)
    if this_year_birthday < today:
        next_birthday = get_birthday_for_year(birthday, today.year + 1)
    else:
        next_birthday = this_year_birthday

    birthday_countdown = (next_birthday - today).days
    return birthday_countdown

def get_birthday_for_year(birthday, year):
    try:
        calculated_birthday = birthday.replace(year=year)
    except ValueError:
        calculated_birthday = date(year=year, month=3, day=1)
    return calculated_birthday