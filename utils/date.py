import sys

from datetime import datetime, timedelta


def date_range(start_date, end_date):
    date_list = []
    start = datetime.strptime(start_date, "%d/%m/%Y")
    end = datetime.strptime(end_date, "%d/%m/%Y")
    current = start
    while current <= end:
        date_list.append(current.date())
        current += timedelta(days=1)
    return date_list


def parse_dates(dates):
    for date in dates.values():
        if not valid_date(date):
            print('Invalid date in settings.toml. Expected format: DD/MM/YYYY')
            sys.exit()

    return date_range(dates['start_date'], dates['end_date'])


def valid_date(date_string):
    try:
        datetime.strptime(date_string, '%d/%m/%Y')
        return True
    except ValueError:
        return False
