month = ['January',
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
         'December'
        ]
month_abbvs = dict((m[:3].lower(),m)for m in month)
def valid_month(month):
    if month:
        cap_month = month.capitalize()
        if cap_month in months:
            return cap_month

print(month)
