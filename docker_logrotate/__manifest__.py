{
    'name': 'Docker Container Logrotate',
    'category': 'Technical Settings',
    'version': '1.0.0',
    'author': 'VTA IT Team',
    'website': 'https://www.viettinhanh.com.vn',
    'depends': ['base_setup'],
    'external_dependencies': {
        'bin': ['logrotate']
    },
    'data': [
        'security/ir.model.access.csv',
        'views/docker_logrotate_views.xml',
        'views/res_config_settings_views.xml',
        'data/docker_logrotate_data.xml',
    ],
}
