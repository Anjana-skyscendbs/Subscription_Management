from odoo import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    group_subscriber_admin = fields.Boolean(string='Subscription Admin', implied_group='subscription_managaement.group_subscriber_admin')
    group_subscriber_user = fields.Boolean(string='Subscription USer', implied_group='subscription_managaement.group_subscriber_user')
    group_subscriber_employee = fields.Boolean(string='Subscription Employee', implied_group='subscription_extended.group_subscription_employee')
    # cancel_days = fields.Integer(string='Cancel Days')
