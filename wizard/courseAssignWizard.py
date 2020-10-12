import logging
_logger = logging.getLogger(__name__)

from odoo import models, api, fields
from odoo.exceptions import UserError

class CourseAssignWizard(model.TrasientModel):
    _name = "course.assign.wizard"
    _description = "Asignacion de cursos a usuario existente"
