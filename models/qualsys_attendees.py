import logging
_logger = logging.getLogger(__name__)

from odoo import models, api, fields
from odoo.exceptions import UserError

class QualsysAttendees(models.Model):
    _name = 'qualsys.attendees'
    _description = 'Alumnos'

    partner_id = fields.Many2one('res.partner', string="No. de lista")
    age = fields.Integer(string="Edad", required = True)