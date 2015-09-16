# -*- coding: utf-8 -*-
from openerp import http

class Academy(http.Controller):
    @http.route('/academy/academy/', auth='public')
    def index(self, **kw):
        courses = http.request.env['openacademy.course'].search([])
        return http.request.render('openacademy.index', {
            'courses': courses,
        })

