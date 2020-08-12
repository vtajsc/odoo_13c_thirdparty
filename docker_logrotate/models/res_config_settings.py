
import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class Settings(models.TransientModel):

    _inherit = 'res.config.settings'

    def _default_docker_logrotate(self):
        Model = self.env['docker.logrotate'].sudo()
        config = Model.search([], limit=1)

        if not config:
            config = Model.create({'config': '/etc/logrotate.d/odoo'})

        return config.id

    docker_logrotate_id = fields.Many2one(
        comodel_name='docker.logrotate',
        string='Logrotate Record',
        default=_default_docker_logrotate)
    docker_logrotate_config = fields.Char(related='docker_logrotate_id.config', readonly=False)
