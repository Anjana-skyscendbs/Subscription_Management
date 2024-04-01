{
    'name': 'Subscription Management',
    'description': 'This module is used to manage subscribers of Channel and Its Information',
    'author': 'Skyscend Trainee Solutions Pvt. Ltd.',
    'website': 'https://www.skyscendbstrainee.com',
    'version': '1.0',
    'summary': 'Manage subscription plans and customer subscriptions',
    'depends': ['base'],
    'data': [
        'security/subscription_security.xml',
        'security/ir.model.access.csv',
        'views/subscription_view.xml',
    ],
    'auto_install': False,
    'installable':True,
    'application': True,
}