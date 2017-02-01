#!/usr/bin/env python

"""
meetup.py

Python script for the Python "Meetup", 'exercism' exercise.

A script to calculate the date of meetups.
Typically meetups happen on the same day of the week.

Examples are
- the first Monday
- the third Tuesday
- the Wednesteenth
- the last Thursday

Created by: shamdela
Date:       22/09/2016
"""
from datetime import date
import calendar


# Constants
WEEKDAYS = {'Monday':0, 'Tuesday':1, 'Wednesday':2, 'Thursday':3, 'Friday':4, 'Saturday':5, 'Sunday':6}
WEEK_NUMBERS = {'1st': 0, '2nd': 1, '3rd': 2, '4th': 3, '5th': 4, 'teenth': None, 'last': None}


class MeetupDayException(Exception):
    """Raise for my specific exception"""


def meetup_day(year, month, dayofweek, week_index):
    day = None

    # Set up calendar and find a matrix of month in question
    cali = calendar.Calendar(firstweekday=0)
    month_matrix = cali.monthdayscalendar(year, month)

    no_of_wks_in_month = len(month_matrix)

    # assign 'last' and 'teenth' keys in dict
    WEEK_NUMBERS['last'] = no_of_wks_in_month - 1 if (month_matrix[no_of_wks_in_month - 1][WEEKDAYS[dayofweek]] > 0) \
        else no_of_wks_in_month - 2
    WEEK_NUMBERS['teenth'] = 2 if (month_matrix[2][WEEKDAYS[dayofweek]] > 0) else 3

    if week_index == 'teenth':
        day = month_matrix[WEEK_NUMBERS['teenth']][WEEKDAYS[dayofweek]]
    else:
        count = 0
        for _, week_row in enumerate(month_matrix):
            if week_row[WEEKDAYS[dayofweek]] > 0:
                if count == WEEK_NUMBERS[week_index]:
                    day = week_row[WEEKDAYS[dayofweek]]
                    break
                count += 1

    if not day:
        raise MeetupDayException()

    return date(year, month, day)


