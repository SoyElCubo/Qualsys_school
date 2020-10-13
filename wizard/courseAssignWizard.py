import logging
_logger = logging.getLogger(__name__)

from odoo import models, api, fields
from odoo.exceptions import UserError

class CourseAssignWizard(models.TransientModel):
    _name = "course.assign.wizard"
    _description = "Asignacion de cursos a usuario existente"

    courses_id = fields.Many2many('qualsys.courses', string="Cursos")

    def asignar_curso(self):
        #_logger.info("#### Aqui se asignan los cursos")

        context = dict(self._context or {})
        _logger.info("Que demonios hay en %s" %context)
        attendees = self.env[context.get('active_model')].browse(context.get('active_ids'))
        #attendees = self.env[context.get('active_model')].search([('id', 'in', context.get('active_ids'))])
        #self.env[nombre del modelo del  cual desean extraer info].browse/.search/.search_count()
        for asignar in self.courses_id:
            asignar.attendees_id |= attendees
            #_logger.info("### Curso: %s" % asignar.attendees_id)
            for curso in attendees:
                curso.courses_id |= asignar
        pass