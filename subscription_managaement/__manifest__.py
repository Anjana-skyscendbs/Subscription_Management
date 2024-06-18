{
    'name': 'Subscription Management',
    'description': 'This module is used to manage student Information',
    'author': 'Skyscend Business Solutions Pvt. Ltd.',
    'website': 'https://www.skyscendbs.com',
    'version': '1.0',
    'depends': ['base','mail','web'],
    'data': [
        'security/sub_manage_security.xml',
        'security/ir.model.access.csv',
        'data/user_sequence.xml',
        'views/subscriber_view.xml',
        'views/plans_view.xml',
        'views/types_view.xml',
        'views/services_view.xml',
        'views/addsubscription_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'subscription_managaement/static/src/scss/test_style.scss'
        ],
    },
    'auto_install': False,
    'installable':True,
    'application': True,
}