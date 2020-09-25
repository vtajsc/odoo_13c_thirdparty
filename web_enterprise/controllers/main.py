
import logging

from odoo import http

from odoo.addons.web.controllers import main

_logger = logging.getLogger(__name__)


class WebClient(main.WebClient):

    @http.route()
    def version_info(self):
        info = super(WebClient, self).version_info()
        info['server_version'] = '13.0+e'
        info['server_version_info'] = list(info['server_version_info'][:-2]) + ['e']
        return info
