import datetime
from aiogram import types
import calendar

from database import DataBase




db = DataBase()


def auth(func):
    async def wrapper(message):
        telegram_id = message.from_user.id 
        user_id = db.check_user(telegram_id)
        if user_id is None:
            return await message.answer("Access closed", reply=False)
        return await func(message)
    return wrapper


def get_button_manicure_basic():
    kb = [[types.KeyboardButton(text="/menu"), types.KeyboardButton(text="/today")]]
    row = db.check_basic()
    if not row is None:
        kb1 = getkeyboards(data=row)
        for k in kb1:
            kb.append(k)
    kb.append([ types.KeyboardButton(text='/month'), types.KeyboardButton(text='/last_month')])
    return "меню", kb


def get_button_manicure_service(data):
    kb = [[types.KeyboardButton(text="/menu"), types.KeyboardButton(text="/today")]]
    row = db.check_service(data=data)
    if not row is None:
        new_row = []
        for r in row:
            new_row.append((r[0], f"{r[0]}){r[1]}"))
        kb1 = getkeyboards(data=new_row)
        for k in kb1:
            kb.append(k)
    return "ок", kb



def parser(message):
    text = message.text
    if text[:1].isdigit():
        digit = text.split(")")[0]
        if digit.isdigit():
            id = int(digit)
            telegram_id = db.check_user(message.from_user.id )
            db.add_provided(id, telegram_id)
            return "Добавил", []
        else:
            id = None
            return "Нет такой записи", []
    else:
        #обратиться к базе и найти запись
        answer, kb = get_button_manicure_service(text)
        return answer, kb



def func():
    if True:
        return True
    return False


def getkeyboards(data):
    keyboards = []
    count = 2
    list_data = []
    for i in range(0, len(data), count):
        for text in data[i:i+count]:
            list_data.append(types.KeyboardButton(text=text[1]))
        keyboards.append(list_data)
        list_data = []
    return keyboards



def getdatatday(day, telegram_id):
    telegram_id = db.check_user(telegram_id)
    row = db.check_provided_day(day=day, telegram_id=telegram_id)
    sum = 0
    answer = ""
    for r in row:
        answer += f"{r[3]} {r[2]} - {r[1]} руб. /del{r[0]}\n"
        sum += r[1]
    answer += f"{sum} руб."
    return answer


def getmonth(day, telegram_id):
    telegram_id = db.check_user(telegram_id)
    first_day, last_day = first_last_day(day)
    row = db.check_provided_month(first_day=first_day, last_day=last_day, telegram_id=telegram_id)
    sum = 0
    answer = ""
    group_provided = {}
    for r in row:
        key = f"{r[2]} {r[1]}"
        if key in group_provided.keys():
            group_provided[key] += r[0]
        else:
            group_provided[key] = r[0]
        sum += r[0]
    
    for k, v in group_provided.items():
        answer += f"{k} - {v} руб. \n"
    answer += f"{sum} руб."
    return answer


def first_last_day(day):
    days = calendar.monthrange(day.year, day.month)
    first_day = datetime.date(day.year, day.month, 1)
    last_day = datetime.date(day.year, day.month, days[1])
    return first_day, last_day


def deleteprovided(id):
    try:
        db.remove_provided(id)
        return "Удалено"
    except:
        return "Ошибка"