
import logging
import traceback

from subprocess import Popen, PIPE

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools import find_in_path

_logger = logging.getLogger(__name__)


class Logrotate(models.Model):

    _name = 'docker.logrotate'
    _description = 'Logrotate process in docker containers'

    _sql_constraints = [
        ('uniq_logrotate_config', 'UNIQUE(active)', 'Duplicate'),
        ('valid_logrotate_config', 'CHECK(active)', 'Invalid'),
    ]

    config = fields.Char(string='File Config', required=True)
    active = fields.Boolean(default=True)

    @api.model
    def _run(self, test_mode=False):
        _logger.info('==========Rotating Server Logfile==========')
        try:
            log = self.search([], limit=0)

            if not log:
                raise UserError('Logrotate config not found')

            executor = find_in_path('logrotate')
            mode = '-d' if test_mode else '-f'
            process = Popen([executor, mode, log.config], stderr=PIPE)
            _, err_msg = process.communicate()

            if process.returncode:
                if err_msg:
                    err_msg = err_msg.decode('unicode_escape')
                else:
                    err_msg = 'Rotating failed with exit code {}'.format(process.returncode)

                raise UserError(err_msg)

            self._log()
            _logger.info('==========Server Logfile Successfully Rotated==========')
        except Exception:
            self._log(traceback.format_exc(chain=False), error=True)
            _logger.info('==========Rotating Server Logfile is Failed==========')

        return True

    @api.model
    def _log(self, msg=False, error=False):
        return self.env['docker.logrotate.log'].sudo().create({
            'date_log': fields.Datetime.now(),
            'state': 'error' if error else 'success',
            'note': msg,
        })


class LogrotateHistory(models.Model):

    _name = 'docker.logrotate.log'
    _description = 'Logrotate logs'
    _order = 'date_log desc'

    date_log = fields.Datetime(string='Log Date', required=True)
    state = fields.Selection(
        selection=[('success', 'Successful!'), ('error', 'Failed!')],
        string='Result', required=True)
    note = fields.Text(string='Details')
