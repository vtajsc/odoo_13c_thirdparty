{
    'name': 'Mobile',
    'summary': 'Odoo Mobile Core module',
    'description': """
    This module provides the core of the Odoo Mobile App.
    """,
    'category': 'Mobile',
    'author': 'Odoo S.A.',
    'version': '1.0',
    'license': 'OEEL-1',
    'depends': ['base_setup'],
    'data': [
        'views/templates.xml',
        'views/res_partner_views.xml',
        'views/res_config_settings_views.xml',
    ],
    'qweb': [
        'static/src/xml/contact_sync.xml',
        'static/src/xml/barcode_fields.xml',
        'static/src/xml/user_menu.xml',
    ],
    'auto_install': True,
}
