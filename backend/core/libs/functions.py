


from datetime import timedelta, date


def get_month():
    today = date.today() + timedelta(days=1)
    first_day_1 = date(today.year, today.month, 1)
    last_month = first_day_1 - timedelta(days=20)
    first_day_2 = date(last_month.year, last_month.month, 1)
    last_month = first_day_2 - timedelta(days=20)
    first_day_3 = date(last_month.year, last_month.month, 1)
    return (first_day_1, today), (first_day_2, first_day_1), (first_day_3, first_day_2)
