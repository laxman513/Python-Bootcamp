import datetime


def current_date():
    return datetime.date.today()


def current_time():
    return datetime.datetime.now().strftime("%H:%M:%S")