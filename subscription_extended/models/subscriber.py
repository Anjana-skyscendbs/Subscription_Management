from odoo import models, fields, api


class Subscriber(models.Model):
    # If you use only _inherit it will add / modify in to existing
    _inherit = 'subscription.user'

    height = fields.Float('Height(cm)')
    weight = fields.Float('Weight(kg)')
    blood_group = fields.Char('Blood Group')
    extra_notes = fields.Html('Extra Notes')