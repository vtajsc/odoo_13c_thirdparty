
import logging

from odoo import models

_logger = logging.getLogger(__name__)


class IrHttp(models.AbstractModel):

    _inherit = 'ir.http'

    def webclient_rendering_context(self):
        return {
            'session_info': self.session_info(),
        }

    def session_info(self):
        info = super(IrHttp, self).session_info()
        info.update({
            'server_version': '%s+e' % info['server_version'].replace('+e', ''),
            'server_version_info': list(info['server_version_info'][:-2]) + ['e'],
        })
        return info
