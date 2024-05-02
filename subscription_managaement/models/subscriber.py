from odoo import models, fields


class Subscriber(models.Model):
    _name = 'subscription.user'
    _description = 'Users'
    _auto = True
    # _order = 'sequence'

    name = fields.Char(string='Name', required=True, index=True, translate=True)
    age = fields.Integer('Age', default=18, group_operator='avg')
    active = fields.Boolean('Active', help='This field is used to activate or deactivate a record', default=True)
    notes = fields.Text('Notes')
    template = fields.Html('Template')
    birthdate = fields.Date('Birthdate')
    timestamp = fields.Datetime('Timestamp', readonly=True)
    gender = fields.Selection(selection=[('male', 'Male'),
                                         ('female', 'Female')], string='Gender')
    # student_code = fields.Char('Student Code', size=4)
    password = fields.Char('Password')
    email = fields.Char('Email')
    url = fields.Char('URL')
    phone = fields.Char('Phone')

    sign_in = fields.Float('Sign In')
    priority = fields.Selection([(str(ele), str(ele)) for ele in range(6)], 'Priority')
    ref = fields.Reference([('subscription.user', ' Subscribers'),
                            ('res.users', 'Users'),
                            ('res.partner', 'Contacts')], 'Reference')

    document = fields.Binary('Document')
    file_name = fields.Char('File Name')
    photo = fields.Image('Photo')

    state = fields.Selection([('applied', 'Applied'),
                              ('done', 'Done'),
                              ('joined', 'Joined'),
                              ('left', 'Left')], 'State', default='applied')
    plan_id = fields.Many2one('subscription.plan', 'Plan')
    type_ids = fields.One2many('subscription.addsubscription', 'user_id', 'Subscriptions')
    service_ids = fields.Many2many('subscription.service', string='Services')
    sequence = fields.Integer('Sequence')
    parent_id = fields.Many2one('subscription.user', 'Monitor')

    child_ids = fields.One2many('subscription.user', 'parent_id', 'Subordinates')
