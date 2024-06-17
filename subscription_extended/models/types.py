from odoo import models,fields,api


class Standard(models.Model):

    _inherit = ['mail.thread','mail.activity.mixin','subscription.type']
    _name = 'subscription.type'

    color = fields.Integer('Color')