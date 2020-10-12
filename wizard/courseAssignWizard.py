import logging
_logger = logging.getLogger(__name__)

from odoo import models, api, fields
from odoo.exceptions import UserError

class CourseAssignWizard(models.TransientModel):
    _name = "course.assign.wizard"
    _description = "Asignacion de cursos a usuario existente"

    courses_id = fields.Many2many('qualsys.courses', string="Cursos")