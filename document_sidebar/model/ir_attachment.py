# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class IrAttachment(models.Model):
    _inherit = 'ir.attachment'

    @api.model
    def create(self, vals):
        if self.env.user.has_group('vta_marketplace_generic.group_vta_hub_staff') and self.env.user.login != 'admin':
            raise UserError(_("You don't have permission for this action"))
        if vals['res_model'] == 'sale.order':
            so_id = self.env['sale.order'].search([('id', '=', vals['res_id'])])
            if so_id:
                so_id._attach_compute()
                if vals['name'] and vals['datas']:
                    pickings = so_id.mapped('picking_ids')
                    for pic in pickings:
                        self.create({
                            'name': vals['name'],
                            'res_id': pic.id,
                            'res_model': pic._name,
                            'datas': vals['datas'],
                            'type': 'binary',
                        })
        res = super(IrAttachment, self).create(vals)
        return res

    def write(self, vals):
        res = super(IrAttachment, self).write(vals)
        if self.env.user.has_group('vta_marketplace_generic.group_vta_hub_staff') and self.env.user.login != 'admin':
            raise UserError(_("You don't have permission for this action"))
        return res

    def unlink(self):
        res = super(IrAttachment, self).unlink()
        if self.env.user.has_group('vta_marketplace_generic.group_vta_hub_staff') and self.env.user.login != 'admin':
            raise UserError(_("You don't have permission for this action"))
        return res
