
import logging

from odoo import tools, models, fields, api

_logger = logging.getLogger(__name__)


class Menu(models.Model):

    _inherit = 'ir.ui.menu'

    is_float = fields.Boolean()

    @api.model
    def _set_is_float(self, menu_root):
        def _filter(rec):
            return rec.id == menu['id']

        if isinstance(menu_root, dict) and 'children' in menu_root:
            root_menus = self.get_user_roots()

            for menu in menu_root['children']:
                menu_rec = root_menus.filtered(_filter)
                menu.update(is_float=menu_rec.is_float)

        return menu_root

    @api.model
    @tools.ormcache_context('self._uid', keys=('lang',))
    def load_menus_root(self):
        menu_root = super(Menu, self).load_menus_root()
        return self._set_is_float(menu_root)

    @api.model
    @tools.ormcache_context('self._uid', 'debug', keys=('lang',))
    def load_menus(self, debug):
        menu_root = super(Menu, self).load_menus(debug)
        return self._set_is_float(menu_root)
