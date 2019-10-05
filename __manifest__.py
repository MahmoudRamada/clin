# -*- coding: utf-8 -*-
{
    'name': "Veterinary Clinic",

    'summary': """
        EquiClinic 
    """,
    'description': """
        EquiClinic
    """,

    'author': "Bilal",
    'category': 'Clinic',
    'version': '1.11.1',

    # any module necessary for this one to work correctly
    'depends': ['account_invoicing','base','mail','document'],

    # always loaded
    'data': [
        'views/seq.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/animal.xml',
        'wizard/mail_compose_message_view.xml',
        'wizard/canelreason.xml',
        'views/appointment.xml',
        'views/evaluation.xml',
        'views/evaluation_stages.xml',
        'views/menu.xml',
        'reports/report.xml',
        'views/email_templates.xml',
        'data/evaluation_stage.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'images': ['static/description/banner.jpg'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
