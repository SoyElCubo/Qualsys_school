import logging
_logger = logging.getLogger(__name__)

from odoo import models, api, fields
from odoo.exceptions import UserError

class SchoolAssignWizard(models.TransientModel):
    _name = "school.assign.wizard"
    _description = "Asignacion de cursos a escuela existente"

    school_id = fields.Many2one('qualsys.school', string="Escuelas")

    def asignar_escuela(self):
        context = dict(self._context or {})
        school = self.env['qualsys.courses'].browse(context.get('active_ids'))
        #_logger.info("#### Que demonios tiene school %s" % school)
        for asignar in self.school_id:
             asignar.courses_id |= school
             for curso in school:
                 curso.school_id |= asignar
        return {}