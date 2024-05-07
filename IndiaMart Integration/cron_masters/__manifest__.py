
{
    "name": "Cron Master",
    'description': """Developing a cron to migrating the records from indiamart to odoo crm""",
    'summary': """cron development for data migration""",
    "category": 'Cron',
    "version": '14.0.1.0.0',
    'author': 'Dilip Kumar',
    'company': 'Scopex',
    'maintainer': 'Scopex',
    'website': "https://www.scopex.in",
    "depends": ['base','mail','crm'],
    "data": [
        'security/ir.model.access.csv',
        'views/key_master_crm.xml',
        'views/cron.xml',
        'views/crm_inherit.xml',

    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}