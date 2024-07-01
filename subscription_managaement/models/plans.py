from odoo import models, fields

class Subscriptionplan(models.Model):
    _name = 'subscription.plan'
    _description = 'Plans'

    name = fields.Char('Name', required=True)
    code = fields.Char('Code', required=True)
    duration = fields.Float('Duration')
    unit = fields.Char('Unit')
    start_timestamp = fields.Datetime('Start Date')
    end_timestamp = fields.Datetime('End Date')
    color =fields.Integer('Colors')