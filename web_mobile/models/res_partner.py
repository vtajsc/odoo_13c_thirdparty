
import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):

    _inherit = 'res.partner'

    image_medium = fields.Binary(related='image_128', string='Medium-sized image')
