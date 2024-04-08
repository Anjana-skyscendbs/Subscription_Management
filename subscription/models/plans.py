from odoo import models, fields

class SchoolStandard(models.Model):
    _name = 'subscription.plans'
    _description = 'Plans'

    name = fields.Char('Name')
    code = fields.Char('Code', size=6)