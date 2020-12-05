import re


def add_time(start, duration, wday=None):
    daysOfTheWeek = {"Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6, "Sunday": 0}
    begin = re.split('[: ]', start)
    add = re.split(':', duration)
    minutes = int(begin[1]) + int(add[1])
    hours = int(add[0])
    if minutes > 59:
        minutes -= 60
        hours += 1
    if begin[2] == "AM":
        if begin[0] == "12":
            hours += 0
        else:
            hours += int(begin[0])
    else:
        if begin[0] == "12":
            hours += 12
        else:
            hours += 12 + int(begin[0])
    print(hours)
    pastDays = int(hours / 24)
    hours = int(hours) % 24
    meridiem = None
    if hours >= 12:
        meridiem = "PM"
        if hours != 12:
            hours -= 12
    else:
        meridiem = "AM"
        if hours == 0:
            hours = 12
    date = str(hours) + ":"
    if minutes < 10:
        date += '0'
    date += str(minutes)
    date += ' ' + meridiem
    if wday is not None:
        wday = wday[0].upper() + wday[1:].lower()
        wday = daysOfTheWeek[wday]
        wday += pastDays
        wday %= 7
        for k, v in daysOfTheWeek.items():
            if v == wday:
                wday = k
                break
        date += ', ' + wday
    if pastDays == 1:
        date += " (next day)"
    elif pastDays > 1:
        date += " (" + str(pastDays) + " days later)"
    return date
