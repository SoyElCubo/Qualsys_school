import logging
_logger = logging.getLogger(__name__)

from odoo import models, api, fields
from odoo.exceptions import UserError

class QualsysCourses(models.Model):
    _name = 'qualsys.courses'
    _description = 'Cursos'

    @api.depends('attendees_id')
    def get_courses_attendees(self):
        for data in self:
            data.attendees_number = len(data.attendees_id)

    name = fields.Char(string = "Nombre del curso", required=True)
    duration = fields.Integer(string="Duracion", required=True)
    start_date = fields.Date(string="Fecha de inicio", required=True)
    end_date = fields.Date(string="Fecha de conclucion", required=True)
    code = fields.Char(string="Codigo de curso", required=True)
    attendees_number = fields.Integer(compute = get_courses_attendees, String="No. de Alumnos")
    school_id = fields.Many2one('qualsys.school', string=" Tipo de curso")
    attendees_id = fields.Many2many('qualsys.attendees', string="Asistentes")
    teacher_id = fields.Many2one('res.users', string="Profesor")


