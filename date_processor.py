from datetime import *


def translate_month_name_to_number(month):
    try:
        months_numbers = {
            'января': '1',
            'февраля': '2',
            'марта': '3',
            'апреля': '4',
            'мая': '5',
            'июня': '6',
            'июля': '7',
            'августа': '8',
            'сентября': '9',
            'октября': '10',
            'ноября': '11',
            'декабря': '12'
        }
        return months_numbers[month]
    except KeyError:
        return None


# https://stackoverflow.com/questions/304256/whats-the-best-way-to-find-the-inverse-of-datetime-isocalendar
def _iso_year_start(iso_year):
    fourth_jan = date(iso_year, 1, 4)
    delta = timedelta(fourth_jan.isoweekday() - 1)
    return fourth_jan - delta


def _iso_to_gregorian(iso_year, iso_week, iso_day):
    year_start = _iso_year_start(iso_year)
    return year_start + timedelta(days=iso_day - 1, weeks=iso_week - 1)


def first_and_last_date_of_week(iso_calendar_tuple):
    # iso_calendar_tuple (year, week_number, weekday)
    first_day_of_week = _iso_to_gregorian(iso_calendar_tuple[0], iso_calendar_tuple[1], 1).isoformat()
    last_day_of_week = _iso_to_gregorian(iso_calendar_tuple[0], iso_calendar_tuple[1], 7).isoformat()
    return (first_day_of_week, last_day_of_week)


def calculate_week_and_week_corner_dates(raw_publish_date):
    date_list = raw_publish_date.strip().split(" ")
    if len(date_list) == 3:
        string_date = date_list[0]
    elif len(date_list) == 4:
        string_date = date_list[0] + " " + translate_month_name_to_number(date_list[1])
    else:
        return None

    if len(string_date.split(' ')) == 2:
        current_year = date.today().year
        current_month = int(string_date.split(' ')[1])
        current_day = int(string_date.split(' ')[0])
        current_date = date(current_year, current_month, current_day)
    else:
        converter = {
            'сегодня': date.today(),
            'вчера': date.today() - timedelta(1)
        }
        current_date = converter[string_date]

    current_week = current_date.isocalendar()[1]

    return (current_week, first_and_last_date_of_week(current_date.isocalendar()))
