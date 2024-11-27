


from datetime import timedelta, date, datetime


def get_month():
    today = date.today() + timedelta(days=1)
    first_day_1 = date(today.year, today.month, 1)
    last_month = first_day_1 - timedelta(days=20)
    first_day_2 = date(last_month.year, last_month.month, 1)
    last_month = first_day_2 - timedelta(days=20)
    first_day_3 = date(last_month.year, last_month.month, 1)
    return (first_day_1, today), (first_day_2, first_day_1), (first_day_3, first_day_2)


def generate_date_list(start_date, end_date=None, weekends=True) -> list:
   if end_date is None:
       end_date = datetime.today().date()
   
   
   if isinstance(start_date, str):
       start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
   if isinstance(end_date, str):
       end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
   
   # Создаем список дат
   date_list = []
   
   # Проверяем порядок дат
   if start_date > end_date:
       return date_list
   
   
   current_date = start_date
   while current_date <= end_date:
       # Проверяем, что день не суббота (5) и не воскресенье (6)
       if weekends or current_date.weekday() < 5:
           date_list.append(current_date)
       current_date += timedelta(days=1)
   return date_list