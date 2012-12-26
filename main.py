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
import cgi
from google.appengine.api import users
import webapp2
import logging
from google.appengine.api import mail


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(
        os.path.join(os.path.dirname(__file__), "templates")))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header_images = [u"cabecera1w.jpg", u"cabecera1w.jpg", u"cabecera2w.jpg", u"cabecera3w.jpg", u"cabecera3w.jpg", u"cabecera4w.jpg"]
        template_values = {
            'page_name': u"Portada",
            'site_name': u"Club In-Line Sancti Petri",
            'site_address': u"http://www.inlinesanctipetri.com",
            'page_description': u"Web informativa del club deportivo Inline Sancti Petri. Club de hockey línea en Chiclana, Cádiz",
            'header_image': random.choice(header_images)
        }
        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render(template_values))

class EscuelasHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'page_name': u"Escuelas",
            'site_name': u"Club In-Line Sancti Petri",
            'page_description': u"Escuelas deportivas de patinaje y hockey línea en el club deportivo Inline Sancti Petri de Chiclana, Cádiz",
            'site_address': u"http://www.inlinesanctipetri.com"
        }
        template = jinja_environment.get_template('escuelas.html')
        self.response.out.write(template.render(template_values))

class CompeticionesHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'page_name': u"Competiciones",
            'site_name': u"Club In-Line Sancti Petri",
            'page_description': u"Calendario de competiciones de hockey línea: ligas, campeonatos y torneos del club deportivo Inline Sancti Petri de Chiclana, Cádiz",
            'site_address': u"http://www.inlinesanctipetri.com"
        }
        template = jinja_environment.get_template('competiciones.html')
        self.response.out.write(template.render(template_values))

class QuienesHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'page_name': u"Quienes Somos",
            'page_description': u"Trayectoria, trofeos, organización y equipo senior de hockey línea del club deportivo Inline Sancti Petri de Chiclana, Cádiz",
            'site_name': u"Club In-Line Sancti Petri",
            'site_address': u"http://www.inlinesanctipetri.com"
        }
        template = jinja_environment.get_template('quienes_somos.html')
        self.response.out.write(template.render(template_values))


class ContactaHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'page_name': u"Contacta",
            'page_description': u"Formulario de contacto del club deportivo de hockey Inline Sancti Petri de Chiclana, Cádiz",
            'site_name': u"Club In-Line Sancti Petri",
            'site_address': u"http://www.inlinesanctipetri.com"
        }

        template = jinja_environment.get_template('contacta.html')
        self.response.out.write(template.render(template_values))

    def post(self):
        mensaje_confirmacion = u'Gracias! Te contesto lo antes posible'
        mensaje = False
        error= False
        # datos del POST
        nombre = self.request.get("nombre")
        email = self.request.get("email")
        comentario = self.request.get("comentario")

        # log ip de envio de email
        logging.info('Peticion de envio de mail desde %s con %s' % (self.request.remote_addr, email))
        # enviar el correo
        email_del_servidor = 'Inline Sancti Petri web <admin@inlinesanctipetri.com>'
        #bcc_email = 'Jesus <jdemula@gmail.com>'
        para = 'Secretario <secretario@inlinesanctipetri.com>'
        titulo_correo = 'Consulta desde la Web'
        texto_email = "Nombre: %s\nRemite: %s\nComentario: %s\n" % (nombre, email, comentario)
        try:
            mail.send_mail(sender=email_del_servidor, to=para,
                    subject=titulo_correo, body=texto_email)
            mensaje = mensaje_confirmacion
        except:
            error= u"Ha habido un error en su peticion"
        finally:
            # respuesta web
            template_values = {
                'page_name': u"Contacta",
                'page_description': u"Formulario de contacto del club deportivo de hockey Inline Sancti Petri de Chiclana, Cádiz",
                'site_name': u"Club In-Line Sancti Petri",
                'site_address': u"http://www.inlinesanctipetri.com",
                'message': mensaje,
                'error': error
            }
            template = jinja_environment.get_template('contacta.html')
            self.response.out.write(template.render(template_values))


class ApuntateHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'page_name': u"Apuntate",
            'page_description': u"Formulario de alta en la lista de correos del club deportivo de hockey Inline Sancti Petri de Chiclana, Cádiz",
            'site_name': u"Club In-Line Sancti Petri",
            'site_address': u"http://www.inlinesanctipetri.com"
        }
        template = jinja_environment.get_template('apuntate.html')
        self.response.out.write(template.render(template_values))

app = webapp2.WSGIApplication([('/', MainHandler),
                              ('/escuelas/', EscuelasHandler),
                              ('/competiciones/', CompeticionesHandler),
                              ('/quienes-somos/', QuienesHandler),
                              ('/contacta/', ContactaHandler),
                              ('/apuntate/', ApuntateHandler),],
                              debug=True)
