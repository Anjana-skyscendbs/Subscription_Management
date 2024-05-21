from odoo import fields,models,api


class SubscriptionType(models.Model):
    _name = 'subscription.type'
    _description = 'Types'

    name = fields.Char('Name', required=True)
    code = fields.Char('Code', required=True)












