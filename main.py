#!/usr/bin/env python

import os
import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
# [END imports]

class Home(webapp2.RequestHandler):
    def get(self):
        self.response.write(JINJA_ENVIRONMENT.get_template('pages/header.html').render({}))
        self.response.write(JINJA_ENVIRONMENT.get_template('pages/index.html').render({}))
        self.response.write(JINJA_ENVIRONMENT.get_template('pages/footer.html').render({}))
        
class BigGameHunting(webapp2.RequestHandler):
    def get(self):
        self.response.write(JINJA_ENVIRONMENT.get_template('pages/header.html').render({}))
        self.response.write(JINJA_ENVIRONMENT.get_template('pages/hunting.html').render({}))
        self.response.write(JINJA_ENVIRONMENT.get_template('pages/footer.html').render({}))
        
class Outfitting(webapp2.RequestHandler):
    def get(self):
        self.response.write(JINJA_ENVIRONMENT.get_template('pages/header.html').render({}))
        self.response.write(JINJA_ENVIRONMENT.get_template('pages/outfitting.html').render({}))
        self.response.write(JINJA_ENVIRONMENT.get_template('pages/footer.html').render({}))
        
class Ranch(webapp2.RequestHandler):
    def get(self):
        self.response.write(JINJA_ENVIRONMENT.get_template('pages/header.html').render({}))
        self.response.write(JINJA_ENVIRONMENT.get_template('pages/ranch.html').render({}))
        self.response.write(JINJA_ENVIRONMENT.get_template('pages/footer.html').render({}))
        
class Contact(webapp2.RequestHandler):
    def get(self):
        self.response.write(JINJA_ENVIRONMENT.get_template('pages/header.html').render({}))
        self.response.write(JINJA_ENVIRONMENT.get_template('pages/contact.html').render({}))
        self.response.write(JINJA_ENVIRONMENT.get_template('pages/footer.html').render({}))

app = webapp2.WSGIApplication([
    ('/', Home),
    ('/hunting', BigGameHunting),
    ('/outfitting', Outfitting),
    ('/ranch', Ranch),
    ('/contact', Contact),
], debug=True)
