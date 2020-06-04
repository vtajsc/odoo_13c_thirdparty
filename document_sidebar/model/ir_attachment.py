# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class IrAttachment(models.Model):
    _inherit = 'ir.attachment'

    @api.model
    def create(self, vals):
        if vals['res_model'] == 'sale.order':
            self.env['sale.order'].search([('id', '=', vals['res_id'])])._attach_compute()
        return super(IrAttachment, self).create(vals)