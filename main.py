#!/usr/bin/env python2
# -*- coding: utf-8 -*-
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
import jinja2
import os
import random
import webapp2

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(
        os.path.join(os.path.dirname(__file__), "templates")))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header_images = ["cabecera1w.jpg", "cabecera1w.jpg", "cabecera2w.jpg", "cabecera3w.jpg", "cabecera3w.jpg", "cabecera4w.jpg"]
        template_values = {
            'page_name': "Portada",
            'site_name': "Club In-Line Sancti Petri",
            'site_address': "http://www.inlinesanctipetri.com",
            'header_image': random.choice(header_images)
        }
        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render(template_values))

class EscuelasHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'page_name': "Escuelas",
            'site_name': "Club In-Line Sancti Petri",
            'site_address': "http://www.inlinesanctipetri.com"
        }
        template = jinja_environment.get_template('escuelas.html')
        self.response.out.write(template.render(template_values))

class SeniorHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'page_name': "Categoria Senior",
            'site_name': "Club In-Line Sancti Petri",
            'site_address': "http://www.inlinesanctipetri.com"
        }
        template = jinja_environment.get_template('senior.html')
        self.response.out.write(template.render(template_values))

class CompeticionesHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'page_name': "Competiciones",
            'site_name': "Club In-Line Sancti Petri",
            'site_address': "http://www.inlinesanctipetri.com"
        }
        template = jinja_environment.get_template('competiciones.html')
        self.response.out.write(template.render(template_values))

class QuienesHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'page_name': "Quienes Somos",
            'site_name': "Club In-Line Sancti Petri",
            'site_address': "http://www.inlinesanctipetri.com"
        }
        template = jinja_environment.get_template('quienes_somos.html')
        self.response.out.write(template.render(template_values))

class ContactaHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'page_name': "Contacta",
            'site_name': "Club In-Line Sancti Petri",
            'site_address': "http://www.inlinesanctipetri.com"
        }
        template = jinja_environment.get_template('contacta.html')
        self.response.out.write(template.render(template_values))

class ApuntateHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'page_name': "Apuntate",
            'site_name': "Club In-Line Sancti Petri",
            'site_address': "http://www.inlinesanctipetri.com"
        }
        template = jinja_environment.get_template('apuntate.html')
        self.response.out.write(template.render(template_values))

class SubscribirHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'page_name': "Subscribir",
            'site_name': "Club In-Line Sancti Petri",
            'site_address': "http://www.inlinesanctipetri.com"
        }
        template = jinja_environment.get_template('subscribir.html')
        self.response.out.write(template.render(template_values))


app = webapp2.WSGIApplication([('/', MainHandler),
                              ('/escuelas/', EscuelasHandler),
                              ('/senior/', SeniorHandler),
                              ('/competiciones/', CompeticionesHandler),
                              ('/quienes-somos/', QuienesHandler),
                              ('/contacta/', ContactaHandler),
                              ('/apuntate/', ApuntateHandler),
                              ('/subscribir/', SubscribirHandler)],
                              debug=True)
