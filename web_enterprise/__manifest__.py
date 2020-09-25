{
    'name': 'Web Enterprise',
    'category': 'Technical Settings',
    'description': """
Odoo Enterprise Web Client.
===========================

This module modifies the web addon to provide Enterprise design and responsiveness.
    """,
    'author': 'Odoo S.A.',
    'version': '1.0',
    'depends': ['web'],
    'auto_install': True,
    'license': 'OEEL-1',
    'data': ['views/templates.xml'],
    'qweb': [
        'static/src/xml/base_mobile.xml',
        'static/src/xml/base.xml',
    ],
}
