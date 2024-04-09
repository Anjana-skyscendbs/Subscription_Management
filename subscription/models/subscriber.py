from odoo import models,fields

class Subscription(models.Model):
    _name ='subscriber.plan'
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
    # recurring_rule_type = fields.Selection([
    #     ('daily', 'Daily'),
    #     ('weekly', 'Weekly'),
    #     ('monthly', 'Monthly'),
    #     ('yearly', 'Yearly')
    # ], string='Recurrence', default='monthly')
    subscriber_code = fields.Char('subscriber Code', size=4)
    password = fields.Char('Password')
    email = fields.Char('Email')
    url = fields.Char('URL')
    phone = fields.Char('Phone')
    sign_in = fields.Float('Sign In')
    review = fields.Selection([(str(ele), str(ele)) for ele in range(5)], 'Review')

    plans_id = fields.Many2one('subscription.plans', 'Plans', ondelete='restrict')

    # subtypes_ids = fields.One2many('subscription.subtypes', 'subscriber_id', 'Types', limit=2)

    premium_ids = fields.Many2many('subscription.premium', string='Premiums')

    ref = fields.Reference([('subscriber.plan', ' Subscribers'),
                            ('res.users', 'Users'),
                            ('res.partner', 'Contacts')], 'Reference')


    currency_id = fields.Many2one('res.currency', 'Currency')
    final_price_amount = fields.Monetary(currency_field='currency_id', string='Price Amount')
    document = fields.Binary('Document')
    file_name = fields.Char('File Name')
    photo = fields.Image('Photo')







