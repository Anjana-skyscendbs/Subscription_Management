from odoo import fields,models,api


class SubscriptionType(models.Model):
    _name = 'subscription.type'
    _description = 'Types'

    name = fields.Char('Name', required=True)
    code = fields.Char('Code', required=True)
    monthly_price = fields.Float('Monthly Price', required=True)
    daily_price = fields.Float('Daily Price', required=True)
    weekly_price = fields.Float('Weekly Price', required=True)
    yearly_price = fields.Float('Yearly Price', required=True)



