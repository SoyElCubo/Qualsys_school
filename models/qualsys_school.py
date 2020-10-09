import logging
_logger = logging.getLogger(__name__)

from odoo import models, api, fields
from odoo.exceptions import UserError

class QualsysSchool(models.Model):
    _name = 'qualsys.school'
    _description = 'Creando el primer modulo'

    @api.depends('courses_id')
    def get_courses_number(self):
         for data in self:
             data.courses_number = len(data.courses_id)

    name = fields.Char(string = "Nombre", required=True)
    street = fields.Char(string="Calle")
    street_number = fields.Char(string="No. ext.")
    city = fields.Char(string="Ciudad", required=True)
    state = fields.Many2one('res.country', string="Estado", required=True)
    country = fields.Many2one('res.country', string="Pais", required=True)
    phone_one = fields.Char(string="Telefono Uno", required=True)
    phone_two = fields.Char(string="Telefono Dos", required=True)
    email = fields.Char(string="Correo electronico")
    courses_number = fields.Integer(compute=get_courses_number, string="No. de Cursos")
    courses_id = fields.One2many('qualsys.courses', 'school_id', string=" Cursos")





