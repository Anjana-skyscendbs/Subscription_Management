from odoo import models, fields

class Subscriptionplan(models.Model):
    _name = 'subscription.recurrence'
    _description = 'Recurrence Period'

    name = fields.Char('Name', required=True)
    code = fields.Char('Code', required=True)
    duration = fields.Float('Duration')
    unit = fields.Char('Unit')