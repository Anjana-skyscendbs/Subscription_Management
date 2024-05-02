from odoo import models, fields,api


class Subscriber(models.Model):
    _name = 'subscription.user'
    _description = 'Users'
    _auto = True
    # _order = 'sequence'

    name = fields.Char(string='Name', required=True, index=True, translate=True)
    age = fields.Integer('Age', default=18, group_operator='avg')
    active = fields.Boolean('Active', help='This field is used to activate or deactivate a record', default=True)
    notes = fields.Text('Notes')
    birthdate = fields.Date('Birthdate')
    timestamp = fields.Datetime('Start Date')
    gender = fields.Selection(selection=[('male', 'Male'),
                                         ('female', 'Female')], string='Gender')
    user_code = fields.Char('User Code', size=4)
    password = fields.Char('Password')
    email = fields.Char('Email')
    phone = fields.Char('Phone')
    ref = fields.Reference([('subscription.user', ' Subscribers'),
                            ('res.users', 'Users'),
                            ('res.partner', 'Contacts')], 'Reference')

    photo = fields.Image('Photo')

    state = fields.Selection([('applied', 'Applied'),
                              ('draft', 'Draft'),
                              ('done', 'Done'),
                              ('left', 'Left')], 'State', default='applied')
    plan_id = fields.Many2one('subscription.plan', 'Plan')
    type_ids = fields.One2many('subscription.addsubscription', 'user_id', 'Subscriptions')
    service_ids = fields.Many2many('subscription.service', string='Services')
    sequence = fields.Integer('Sequence')


    total_subscription_price = fields.Float(string='Total Price',
                                            compute='_compute_total_subscription_price', store=True)

    @api.depends('type_ids.price_depend')
    def _compute_total_subscription_price(self):
        for user in self:
            user.total_subscription_price = sum(subscription.price_depend for subscription in user.type_ids)