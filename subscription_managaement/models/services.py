from odoo import fields,models


class SubscriptionServices(models.Model):
    _name = 'subscription.service'
    _description = 'Services'

    name = fields.Char('Name')
    plan_id = fields.Many2one('subscription.plan','Plan')