# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class IrAttachment(models.Model):
    _inherit = 'ir.attachment'

    @api.model
    def create(self, vals):
        result = super(IrAttachment, self).create(vals)
        if result.res_model in ['sale.order']:
            self.env['sale.order'].search([('id', '=', result.res_id)])._attach_compute()
        return result
