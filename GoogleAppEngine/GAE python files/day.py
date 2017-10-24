#!/usr/bin/python
# -*- coding: utf-8 -*-



def valid_day(day):
    if day and day.isdigit():
        day = int(day)
        if day > 0 and day <= 31:
            return day
        
print (valid_day('19'))



