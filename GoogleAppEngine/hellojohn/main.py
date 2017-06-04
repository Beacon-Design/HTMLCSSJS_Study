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

def escape_text(t):
	return cgi.escape(t, quote = True)

form = """
   <form method="post">
        Enter your text
        <br>
        <textarea name="q">%(Area)s</textarea>
        <div style="color: red">%(Error)s</div>
       <input type="submit">
   </form>

"""



class MainPage(webapp2.RequestHandler):
	def write_form(self, error="", area=""):
		self.response.out.write(form % {"Error": error,
										"Area": area,})


	def get(self):
		self.write_form()

	def post(self):
		text = self.request.get("q")
		eText = escape_text(text)
		if not text:
			self.write_form("Bad!", text)
		else:
			self.write_form(error=eText)





			# self.redirect("/thanks")






class ThanksPage(webapp2.RequestHandler):
	def get(self):
		self.response.out.write("thanks")

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/thanks', ThanksPage)
], debug=True)
