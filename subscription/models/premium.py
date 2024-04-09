from odoo import fields,models


class Subscriptionpremium(models.Model):
    _name = 'subscription.premium'
    _description = 'Premium'

    name = fields.Char('Name')