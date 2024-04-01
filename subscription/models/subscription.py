from odoo import models,fields

class Subscription(models.Model):
    _name ='subscription.subscriber'
    _description ='Subscription plan'
    _auto = True

    name = fields.Char(string='Name', required=True)
    age = fields.Integer('Age', default=20)
    active = fields.Boolean('Active', help='This field is used to activate or deactivate a record', default=True)
    price = fields.Float('Price', digits=(16, 2))
    description = fields.Text(string='Description')
    template = fields.Html('Template')
    birthdate = fields.Date('Birthdate')
    start_date = fields.Datetime(string='Start Date', default=fields.Date.today(), required=True)
    gender = fields.Selection(selection=[('male', 'Male'),
                                         ('female', 'Female')], string='Gender')
    recurring_rule_type = fields.Selection([
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly')
    ], string='Recurrence', default='monthly')
    subscriber_code = fields.Char('subscriber Code', size=4)
    password = fields.Char('Password')
    email = fields.Char('Email')
    url = fields.Char('URL')
    phone = fields.Char('Phone')
    sign_in = fields.Float('Sign In')
    review = fields.Selection([(str(ele), str(ele)) for ele in range(5)], 'Review')





