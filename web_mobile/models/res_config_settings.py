
import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class Settings(models.TransientModel):

    _inherit = 'res.config.settings'

    module_ocn_client = fields.Boolean('Push Notifications')
