from odoo import models, fields

class Subscriptionplan(models.Model):
    _name = 'subscription.recurrence'
    _description = 'Recurrence Period'

    name = fields.Char('Name', required=True)
    code = fields.Char('Code', required=True)
    duration = fields.Float('Duration')
    unit = fields.Char('Unit')
    start_timestamp = fields.Datetime('Start Date')
    end_timestamp = fields.Datetime('End Date')
    color = fields.Integer('Color')

