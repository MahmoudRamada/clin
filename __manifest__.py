# -*- coding: utf-8 -*-
{
    'name': " Clinic",

    'summary': """
        Mallgates  """,

    'author': "Mahmoud",
    'category': 'Clinic',
    'description': """ clinci admin App """,

    # any module necessary for this one to work correctly
    'depends': ['account_invoicing','base','mail','document'],

    # always loaded
    'data': [
        'views/seq.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/patient.xml',
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
