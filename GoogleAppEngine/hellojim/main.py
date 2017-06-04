#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi

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


def valid_month(month):
    if month:
        short_month = month[:3].lower()
        return month_abbvs.get(short_month)


def valid_day(day):
    if day and day.isdigit():
        day = int(day)
        if day > 0 and day <= 31:
            return day


def valid_year(year):
    if year and year.isdigit():
        year = int(year)
        if year > 0 and year < 9000:
            return year


def escape_html(s):
    return cgi.escape(s, quote=True)


form = """
   <form method="post">
        what is your birthday?
        <br>
        <label>Month <input type="text" name="MontH" value="%(MONTH)s"> </label>
        <label>Day <input type="text" name="DaY" value="%(DAY)s"> </label>
        <label>Year <input type="text" name="YeaR" value="%(YEAR)s"> </label>
        <div style="color: red">%(ERROR)s<div>
        <br>
        <br>
       <input type="submit">
   </form>

"""


class MainPage(webapp2.RequestHandler):
    def write_form(self, error="", month="", day="", year=""):
        self.response.out.write(form % {"ERROR": error,
                                        "MONTH": escape_html(month),
                                        "DAY": escape_html(day),
                                        "YEAR": escape_html(year)})

    def get(self):
        self.write_form()

    def post(self):
        user_month = self.request.get('MontH')
        user_day = self.request.get('DaY')
        user_year = self.request.get('YeaR')

        month = valid_month(user_month)
        day = valid_day(user_day)
        year = valid_year(user_year)

        if not (month and day and year):
            self.write_form("Bad error!", user_month, user_day, user_year)
        else:
            self.redirect("/thanks")

class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("thanks")

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/thanks', ThanksHandler)
], debug=True)
