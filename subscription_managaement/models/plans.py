from odoo import models, fields

class Subscriptionplan(models.Model):
    _name = 'subscription.plan'
    _description = 'Plans'

    name = fields.Char('Name', required=True)
    code = fields.Char('Code', required=True)