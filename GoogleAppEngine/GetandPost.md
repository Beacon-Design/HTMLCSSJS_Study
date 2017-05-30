

## Get

main.py

```python
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

form="""
   <form action="/testform">
       <input name="q">
       <input type="submit">
   </form>

"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(form)

class TestHandler(webapp2.RequestHandler):
    def get(self):
        # q = self.request.get("q")
        # self.response.write(q)

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(self.request)

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/testform', TestHandler)
], debug=True)

```



## Post

> **Post request should use form**

main.py

```python
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

form="""
   <form method="post" action="/testform">
       <input name="q">
       <input type="submit">
   </form>

"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(form)

class TestHandler(webapp2.RequestHandler):
    def post(self):
        # q = self.request.get("q")
        # self.response.write(q)

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(self.request)

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/testform', TestHandler)
], debug=True)

```



## Solutions to users entering bad data into our form?

> use dropdown to limit what the user can actually enter
>
> verify what the user enter and complain if the data is bad



## Basic Get & Post

> hellojim > main.py

```python
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

form="""
   <form method="post">
        what is your birthday?
        <br>
        <label>Month
        <input type="text" name="month">
        </label>
        
        <label>Day
        <input type="text" name="day">
        </label>
        
        <label>Year
        <input type="text" name="year">
        </label>
        
        <br>
        <br>
       <input type="submit">
   </form>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(form)
    
    def post(self):
        self.response.write("Thanks! That's a totally valid day!")

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
```



## Responding Based On Verification

```python
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

form="""
   <form method="post">
        what is your birthday?
        <br>
        <label>Month
        <input type="text" name="month">
        </label>
        
        <label>Day
        <input type="text" name="day">
        </label>
        
        <label>Year
        <input type="text" name="year">
        </label>
        
        <br>
        <br>
       <input type="submit">
   </form>

"""

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
        if year > 1900 and year < 2020:
            return year

class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.out.write(form)
    
    def post(self):
        user_month = valid_month(self.request.get('month'))
        user_day = valid_day(self.request.get('day'))
        user_year = valid_year(self.request.get('year'))

        if not (user_month and user_day and user_year):
            self.response.write(form)
        else:
            self.response.write("Thanks! That's a totally valid day")
        # self.response.out.write("Thanks! That's a totally valid day")

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)

```



## %s Verification

```python
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
        if year > 1900 and year < 2020:
            return year


form="""
   <form method="post">
        what is your birthday?
        <br>
        <label>Month <input type="text" name="month"></label>
        <label>Day <input type="text" name="day"></label>
        <label>Year <input type="text" name="year"></label>
        <div style="color: red">%(ERROR)s<div>
        <br>
        <br>
       <input type="submit">
   </form>

"""

class MainPage(webapp2.RequestHandler):
    def write_form(self, error=""):
        self.response.out.write(form % {"ERROR": error})

    def get(self):
        self.write_form()
    
    def post(self):
        user_month = valid_month(self.request.get('month'))
        user_day = valid_day(self.request.get('day'))
        user_year = valid_year(self.request.get('year'))

        if not (user_month and user_day and user_year):
            self.write_form("Bad error!")
        else:
            self.response.write("Thanks! That's a totally valid day")
        # self.response.out.write("Thanks! That's a totally valid day")

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
```











