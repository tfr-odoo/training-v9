# -*- coding: utf-8 -*-

from openerp import models, fields, api

class openacademy(models.Model):
    _name = 'openacademy.course'

    name = fields.Char(name='Title', required=True)
    description = fields.Text()
    responsible_id = fields.Many2one('res.users', ondelete='set null', string="Responsible", index=True)
    session_ids = fields.One2many('openacademy.session', 'course_id', string="Sessions")
    level = fields.Selection([(1, 'Easy'), (2, 'Medium'), (3, 'Hard')], string="Difficulty Level")

class Session(models.Model):
    _name = 'openacademy.session'

    name = fields.Char(required=True)
    start_date = fields.Date(default=lambda self : fields.Date.today())
    active = fields.Boolean(default=True)
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    instructor_id = fields.Many2one('res.partner', string="Instructor") #No ondelete = set null
    course_id = fields.Many2one('openacademy.course', ondelete='cascade', string="Course", required=True)
    attendee_ids = fields.Many2many('res.partner', string="Attendees", domain=[('company_type', '=', 'person')])
    taken_seats = fields.Float(string="Taken seats", compute='_taken_seats')
    level = fields.Selection(related='course_id.level')

    @api.one
    @api.depends('seats', 'attendee_ids')
    def _taken_seats(self):
        if not self.seats:
            self.taken_seats = 0.0
        else:
            self.taken_seats = 100.0 * len(self.attendee_ids) / self.seats


    @api.onchange('seats', 'attendee_ids')
    def _verify_valid_seats(self):
        def _warning(title, message):
            return {
              'warning': {
                'title': title,
                'message': message,
              },
            }

        if self.seats < 0:
            return _warning("Incorrect 'seats' value",  "The number of available seats may not be negative")
        if self.seats < len(self.attendee_ids):
            return _warning("Too many attendees", "Increase seats or remove excess attendees")
