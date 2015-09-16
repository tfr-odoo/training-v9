# -*- coding: utf-8 -*-
from openerp import http

class Academy(http.Controller):

    @http.route('/academy/course/', auth='public', website=True)
    def course(self, **kw):
        courses = http.request.env['openacademy.course'].search([])
        return http.request.render('openacademy.course', {
            'courses': courses,
        })

    @http.route('/academy/session/', auth='public')
    def session(self, **kw):
        sessions = http.request.env['openacademy.session'].search([])
        return http.request.render('openacademy.session', {
            'sessions': sessions,
        })

