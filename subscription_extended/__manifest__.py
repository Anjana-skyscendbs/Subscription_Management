{
    'name': 'Subscription Management',
    'description': 'This module is used to manage subscription Information',
    'author': 'Skyscend Business Solutions Pvt. Ltd.',
    'website': 'https://www.skyscendbs.com',
    'version': '1.0',
    'depends': ['base', 'mail','web','subscription_managaement'],
    'data': [
        'security/subscription_security.xml',
        'security/ir.model.access.csv',
        'views/subscriber_view.xml',
        'views/employee_view.xml',
        'views/type_view.xml',
    ],
    'auto_install': False,
    'installable': True,
    'application': True,
}
