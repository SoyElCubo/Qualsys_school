import logging
_logger = logging.getLogger(__name__)

from odoo import models, api, fields
from odoo.exceptions import UserError

class QualsysCourses(models.Model):
    _name = 'qualsys.courses'
    _description = 'Cursos'

    name = fields.Char(string = "Nombre del curso", required=True)
    school_id = fields.Many2one('qualsys.school', string=" Tipo de curso")

