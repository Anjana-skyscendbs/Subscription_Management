from odoo import fields,models


class Subscriptionpremium(models.Model):
    _name = 'subscription.services'
    _description = 'Services'

    name = fields.Char('Name')
    type_id = fields.Many2one('subscription.plans', 'Plans')