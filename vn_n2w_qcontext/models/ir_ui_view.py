
import logging

from odoo import models, api

from . import utils

_logger = logging.getLogger(__name__)


class View(models.Model):

    _inherit = 'ir.ui.view'

    @api.model
    def _prepare_qcontext(self):
        """Add function convert number to words into qcontext."""
        qcontext = super(View, self)._prepare_qcontext()
        def n2w(n, cap=True):
            s = utils.n2w(n)
            if cap:
                s = s[:1].upper() + s[1:]
            return s
        qcontext['vn_n2w'] = n2w
        return qcontext
