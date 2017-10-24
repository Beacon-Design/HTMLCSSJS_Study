#!/usr/bin/python
# -*- coding: utf-8 -*-

months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
    ]
month_abbvs = dict((m[:3].lower(), m) for m in months)


def valid_month_v1(month):
    if month:
        cap_month = month.capitalize()
        if cap_month in months:
            return cap_month
print (valid_month_v1('june'))


def valid_month_v2(month):
    if month:
        short_month = month[:3].lower()
        return month_abbvs.get(short_month)
print(valid_month_v2('jan'))


