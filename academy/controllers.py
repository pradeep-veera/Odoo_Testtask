# -*- coding: utf-8 -*-
from openerp import http
from werkzeug.routing import Map, Rule

class Academy(http.Controller):
    @http.route('/academy/academy/', auth='public', website=True)
    def index(self, **kw):
        Teachers = http.request.env['academy.teachers']
        return http.request.render('academy.index', {
            'teachers': Teachers.search([])
        })



    @http.route('/academy/<name>/', auth='public', website=True)
    def teacher(self, name):
       return  http.request.render('academy.index',{'name':name})

