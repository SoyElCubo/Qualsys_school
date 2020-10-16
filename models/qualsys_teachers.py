from odoo import models, api, fields
from odoo.exceptions import UserError

class QualsysTeachers(models.Model):
    _name = 'qualsys.teachers'
    _description = 'Profesores'

    profesor_name = fields.Char(string="Nombre")
    age = fields.Integer(string="edad")
