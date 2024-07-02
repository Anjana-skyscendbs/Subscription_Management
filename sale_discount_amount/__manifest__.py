{
    'name': 'Sale Discount Amount',
    'version': '1.0',
    'summary': 'Add discount amount to Sale Order Lines and Invoice Lines',
    'description': 'This module adds a discount amount field to Sale Order Lines and Invoice Lines.',
    'category': 'Sales',
    'author': 'Your Name',
    'depends': ['sale', 'account'],
    'data': [
        'views/sale_order_views.xml',
        'views/account_move_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
